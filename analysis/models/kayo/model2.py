import pandas as pd
import numpy as np
import os
from google.cloud import bigquery
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from apyori import apriori

# =========================
# LOAD DATA
# =========================


# Import the data from Google Cloud 
RAW_PATH = "data/raw/feedzai/Base_preview_100.csv"
PROCESSED_DIR = "data/processed"
FIG_DIR = "figures"

os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "fraud-detection-key.json")
    )
client = bigquery.Client(project="csci-4022")
df = client.query("SELECT * FROM `csci-4022.CSCI.fraud_data`").to_dataframe()


#df = pd.read_csv("data/raw/feedzai/Base.csv")

# columns where -1 means missing
maybe_missing_cols = [
    "prev_address_months_count",
    "bank_months_count"
]

# replace -1 with NaN
for col in maybe_missing_cols:
    df[col] = df[col].replace(-1, np.nan)

print("Shape:", df.shape)
print("\nFraud distribution:\n", df["fraud_bool"].value_counts(normalize=True))
print("\nTop missing values:\n", df.isna().sum().sort_values(ascending=False).head(10))

# =========================
# DECISION TREE
# =========================

y = df["fraud_bool"]
X = df.drop(columns=["fraud_bool"])

num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object"]).columns

# fill numeric
X[num_cols] = X[num_cols].fillna(X[num_cols].median())

# keep meaningful missing
for col in maybe_missing_cols:
    X[col] = X[col].fillna(-1)

# fill categorical
X[cat_cols] = X[cat_cols].fillna("unknown")

# encode
X = pd.get_dummies(X, columns=cat_cols, drop_first=True)

print("\nEncoded shape:", X.shape)

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# model
dt = DecisionTreeClassifier(
    max_depth=5,
    class_weight="balanced",
    random_state=42
)

dt.fit(X_train, y_train)

# evaluate
y_pred = dt.predict(X_test)

print("\n=== DECISION TREE ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, digits=4))

# feature importance
importance = pd.Series(dt.feature_importances_, index=X.columns)
print("\nTop 10 Features:\n", importance.sort_values(ascending=False).head(10))

# =========================
# DECISION TREE NOTES
# =========================
# Dataset is highly imbalanced (~1.1% fraud)
# High recall (~74%) but low precision (~3%)
# Model prioritizes catching fraud at cost of false positives
# Top features relate to behavior + identity stability, not just finance

# =========================
# K-MEANS (SAMPLED)
# =========================

df_km = df.sample(n=100000, random_state=42)

X_kmeans = df_km[num_cols].copy()
X_kmeans = X_kmeans.fillna(X_kmeans.median())

for col in maybe_missing_cols:
    X_kmeans[col] = X_kmeans[col].fillna(-1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_kmeans)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

df_km["cluster"] = clusters

print("\n=== KMEANS ===")
print("\nFraud rate by cluster:\n", df_km.groupby("cluster")["fraud_bool"].mean())
print("\nCluster sizes:\n", df_km["cluster"].value_counts())

# =========================
# KMEANS NOTES
# =========================
# Clustering reveals distinct behavioral groups
# One cluster shows significantly higher fraud risk
# Fraud is not random — concentrated in specific groups

# =========================
# APRIORI
# =========================

df_ap = df.sample(n=5000, random_state=42)

df_ap["income_bin"] = pd.qcut(
    df_ap["income"],
    3,
    labels=["low_income", "mid_income", "high_income"]
)

df_ap["credit_bin"] = pd.qcut(
    df_ap["credit_risk_score"],
    3,
    labels=["low_risk", "mid_risk", "high_risk"]
)

transactions = []

for _, row in df_ap.iterrows():
    transactions.append([
        str(row["income_bin"]),
        str(row["credit_bin"]),
        "fraud_" + str(row["fraud_bool"])
    ])

rules = apriori(
    transactions,
    min_support=0.005,
    min_confidence=0.1,
    min_lift=1.0,
    max_length=2
)

print("\n=== APRIORI (FRAUD RULES ONLY) ===")

count = 0
for rule in rules:
    for stat in rule.ordered_statistics:
        if "fraud_1" in stat.items_add:
            base = list(stat.items_base)
            add = list(stat.items_add)
            conf = stat.confidence
            lift = stat.lift
            support = rule.support

            print(
                f"{base} -> {add} | support={support:.3f}, "
                f"confidence={conf:.3f}, lift={lift:.3f}"
            )
            count += 1

        if count >= 5:
            break
    if count >= 5:
        break

if count == 0:
    print("No fraud-related rules found under the current thresholds.")
# =========================
# APRIORI NOTES
# =========================
# Finds combinations of behaviors linked to risk
# Risk is driven by multiple interacting features
# Not limited to low-income or unstable users

# =========================
# FINAL COMPARISON
# =========================
# Decision Tree = best for prediction
# KMeans = shows natural groupings of risk
# Apriori = shows behavioral combinations
# Together → full understanding of fraud behavior