import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, silhouette_score
from sklearn.metrics import davies_bouldin_score
from sklearn.decomposition import PCA

from apyori import apriori

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("data/raw/feedzai/Base.csv")

# columns where -1 may represent missing values
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
# FRAUD DISTRIBUTION VISUAL
# =========================
plt.figure(figsize=(6, 4))
sns.countplot(x=df["fraud_bool"])
plt.title("Fraud vs Non-Fraud Distribution")
plt.xlabel("Fraud Label")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# =========================
# DECISION TREE
# =========================
y = df["fraud_bool"]
X = df.drop(columns=["fraud_bool"])

num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object"]).columns

# fill numeric missing values with median
X[num_cols] = X[num_cols].fillna(X[num_cols].median())

# preserve meaningful missingness for selected columns
for col in maybe_missing_cols:
    X[col] = X[col].fillna(-1)

# fill categorical missing values
X[cat_cols] = X[cat_cols].fillna("unknown")

# one-hot encode categorical variables
X = pd.get_dummies(X, columns=cat_cols, drop_first=True)

print("\nEncoded shape:", X.shape)

# split data
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

# predictions
y_pred = dt.predict(X_test)

print("\n=== DECISION TREE ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, digits=4))

# confusion matrix visual
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Decision Tree Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.tight_layout()
plt.show()

# feature importance
importance = pd.Series(dt.feature_importances_, index=X.columns)
top_features = importance.sort_values(ascending=False).head(10)

print("\nTop 10 Features:\n", top_features)

plt.figure(figsize=(8, 5))
top_features.sort_values().plot(kind="barh")
plt.title("Top 10 Important Features (Decision Tree)")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()

# simplified tree plot
plt.figure(figsize=(16, 8))
plot_tree(
    dt,
    max_depth=3,
    filled=True,
    feature_names=X.columns,
    class_names=["Non-Fraud", "Fraud"],
    fontsize=8
)
plt.title("Decision Tree (Simplified View)")
plt.show()

# =========================
# DECISION TREE NOTES
# =========================
# Dataset is highly imbalanced (~1.1% fraud)
# High recall may come at the cost of low precision
# Model prioritizes catching fraud, even if false positives increase
# Top features may reflect behavioral and identity stability patterns

# =========================
# K-MEANS (SAMPLED)
# =========================
df_km = df.sample(n=100000, random_state=42).copy()

X_kmeans = df_km[num_cols].copy()
X_kmeans = X_kmeans.fillna(X_kmeans.median())

for col in maybe_missing_cols:
    X_kmeans[col] = X_kmeans[col].fillna(-1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_kmeans)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)
sil_score = silhouette_score(X_scaled, clusters)
print("\nSilhouette Score:", sil_score)
db_score = davies_bouldin_score(X_scaled, clusters)
print("Davies-Bouldin Index:", db_score)

df_km["cluster"] = clusters

print("\n=== KMEANS ===")
print("\nFraud rate by cluster:\n", df_km.groupby("cluster")["fraud_bool"].mean())
print("\nCluster sizes:\n", df_km["cluster"].value_counts())

# fraud rate by cluster visual
cluster_fraud = df_km.groupby("cluster")["fraud_bool"].mean()

plt.figure(figsize=(6, 4))
cluster_fraud.plot(kind="bar")
plt.title("Fraud Rate by Cluster")
plt.xlabel("Cluster")
plt.ylabel("Fraud Rate")
plt.tight_layout()
plt.show()

# cluster size visual
plt.figure(figsize=(6, 4))
df_km["cluster"].value_counts().sort_index().plot(kind="bar")
plt.title("Cluster Sizes")
plt.xlabel("Cluster")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# PCA projection for cluster visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, alpha=0.6)
plt.title("KMeans Clusters (PCA Projection)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.tight_layout()
plt.show()

# =========================
# KMEANS NOTES
# =========================
# Clustering reveals distinct behavioral groups
# One cluster may show noticeably higher fraud risk
# Fraud is not evenly distributed across the population

# =========================
# APRIORI
# =========================
df_ap = df.sample(n=5000, random_state=42).copy()

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

fraud_rules = []
count = 0

for rule in rules:
    for stat in rule.ordered_statistics:
        if "fraud_1" in stat.items_add:
            base = list(stat.items_base)
            add = list(stat.items_add)
            conf = stat.confidence
            lift = stat.lift
            support = rule.support

            fraud_rules.append({
                "base": ", ".join(base) if base else "None",
                "add": ", ".join(add),
                "support": support,
                "confidence": conf,
                "lift": lift
            })

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

# apriori visualization
if len(fraud_rules) > 0:
    rules_df = pd.DataFrame(fraud_rules)

    plt.figure(figsize=(8, 5))
    sns.barplot(data=rules_df, x="lift", y="base")
    plt.title("Top Fraud-Related Apriori Rules by Lift")
    plt.xlabel("Lift")
    plt.ylabel("Rule Base")
    plt.tight_layout()
    plt.show()

# =========================
# APRIORI NOTES
# =========================
# Apriori finds combinations of traits linked to fraud
# This helps show that risk may come from interacting behaviors
# It supports interpretation rather than direct prediction

# =========================
# FINAL COMPARISON
# =========================
print("\n=== FINAL COMPARISON ===")
print("Decision Tree = best for prediction")
print("KMeans = shows natural groupings of risk")
print("Apriori = shows behavioral combinations")
print("Together = fuller understanding of fraud behavior")