import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import scipy.stats as stats


RAW_PATH = "data/raw/Base_preview_100.csv"
PROCESSED_DIR = "data/processed"
FIG_DIR = "figures"

os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

#Loading dataset
df = pd.read_csv(RAW_PATH)

#Saving before snapshot
df.head(10).to_csv(f"{PROCESSED_DIR}/before_snapshot.csv", index=False)

#Replacing -1 values with NAN
sentinel_cols = [
    'prev_address_months_count',
    'intended_balcon_amount',
    'bank_months_count',
    'device_distinct_emails_8w'
]

df[sentinel_cols] = df[sentinel_cols].replace(-1, np.nan)

#Categorizing column types
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

#Eliminating fraud target from numeric list
if "fraud_bool" in numeric_cols:
    numeric_cols.remove("fraud_bool")

#Data Preprocessing
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_cols),
        ("cat", categorical_transformer, categorical_cols)
    ]
)


cleaned = preprocessor.fit_transform(df)

#Converting cleaned data into dataframe
cleaned_df = pd.DataFrame(
    cleaned.toarray() if hasattr(cleaned, "toarray") else cleaned
)

#Saving cleaned dataset
cleaned_df.to_csv(f"{PROCESSED_DIR}/cleaned_feedzai.csv", index=False)

#Saving after snapshot
cleaned_df.head(10).to_csv(f"{PROCESSED_DIR}/after_snapshot.csv", index=False)

# Visualizations

#Fraud distribution
plt.figure(figsize=(6,4))
sns.countplot(x='fraud_bool', data=df)
plt.title("Fraud vs Non-Fraud Distribution")
plt.savefig(f"{FIG_DIR}/fraud_distribution.png")
plt.close()

#Correlation heatmap
plt.figure(figsize=(14,10))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig(f"{FIG_DIR}/correlation_heatmap.png")
plt.close()

#Payment type frequency
plt.figure(figsize=(8,4))
sns.countplot(y='payment_type', data=df)
plt.title("Payment Type Frequency")
plt.savefig(f"{FIG_DIR}/payment_type_frequency.png")
plt.close()

#Velocity distributions
df[['velocity_6h','velocity_24h','velocity_4w']].hist(figsize=(12,6))
plt.suptitle("Velocity Feature Distributions")
plt.savefig(f"{FIG_DIR}/velocity_distributions.png")
plt.close()

#QQ plot for income
plt.figure(figsize=(6,6))
stats.probplot(df['income'], dist="norm", plot=plt)
plt.title("QQ Plot: Income")
plt.savefig(f"{FIG_DIR}/qq_income.png")
plt.close()
