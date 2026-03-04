import pandas as pd

#Reading in data
raw_data_path = '../data/raw/feedzai/Base.csv'
raw_data = pd.read_csv(raw_data_path)

#looking at data
print(raw_data.head().T)
print(raw_data.describe().T)

print(f"The fraud distribution in the dataset is as follows: {raw_data['fraud_bool'].value_counts()}")
print(f"The normalized fraud distribution in the dataset is as follows: {raw_data['fraud_bool'].value_counts(normalize=True)}")

#figuring out where the missing data is, there are no missing values, only negative values
missing_data = raw_data == -1
missing_counts = missing_data.sum()
print("Missing values per column:")
print(missing_counts[missing_counts > 0])
print("\nMissing values percentage:")
print((missing_counts[missing_counts > 0] / raw_data.shape[0]) * 100)

#Identifying missing address data
missing_address_data = raw_data[raw_data['prev_address_months_count'] < 0]
missing_address_fraud_column = missing_address_data['fraud_bool']
missing_address_fraud_rate = missing_address_fraud_column.mean()
print(f"\nAudit Result:")
print(f"Number of people with missing addresses: {len(missing_address_data)}")
print(f"Fraud rate for this group: {missing_address_fraud_rate:.2%}")

#Identifying Missing Credit Scores
missing_credit_scores = raw_data[raw_data['credit_risk_score'] < 0]
missing_scores_fraud_column = missing_credit_scores['fraud_bool']
missing_scores_fraud_rate = missing_scores_fraud_column.mean()
print(f"\nAudit Result:")
print(f"Number of people with missing credit scores: {len(missing_credit_scores)}")
print(f"Fraud rate for this group: {missing_scores_fraud_rate:.2%}")

#Fraud Correlation
fraud_correlations = raw_data.corr(numeric_only=True)['fraud_bool'].sort_values(ascending=False)
print("Top Correlations with Fraud:")
print(fraud_correlations[1:6]) 

print("\nStrongest Negative Correlations with Fraud:")
print(fraud_correlations.tail(5))

#Bias Checking
income_bias_check = raw_data.groupby('fraud_bool')['income'].mean()
age_bias_check = raw_data.groupby('fraud_bool')['customer_age'].mean()
credit_bias_check = raw_data.groupby('fraud_bool')['credit_risk_score'].mean()
employment_fraud = pd.crosstab(raw_data['employment_status'], raw_data['fraud_bool'])
housing_status = pd.crosstab(raw_data['housing_status'], raw_data['fraud_bool'])
payment_type = pd.crosstab(raw_data['payment_type'], raw_data['fraud_bool'])
has_other_cards = pd.crosstab(raw_data['has_other_cards'], raw_data['fraud_bool'])
foreign_request = pd.crosstab(raw_data['foreign_request'], raw_data['fraud_bool'])

print("\nAverage Income by Fraud Status:")
print(income_bias_check)

print("\nAverage Age by Fraud Status:")
print(age_bias_check)

print("\nAverage Credit Score by Fraud Status:")
print(credit_bias_check)

print("\nFraud Counts by Employment Status:")
print(employment_fraud)

print("\nFraud Counts by Housing Status:")
print(housing_status)

print("\nFraud Counts by Payment Type:")
print(payment_type)

print("\nFraud Counts by Other Card Status:")
print(has_other_cards)

print("\nFraud Counts by Foreign Request Status:")
print(foreign_request)

#Summary statistics:
#Top 3 positive and negative correlations
numerical_data_stats = raw_data[['customer_age', 'credit_risk_score','income', 'has_other_cards', 'name_email_similarity','date_of_birth_distinct_emails_4w']].agg(['mean', 'median', 'var', 'skew'])
print("\nNumerical Statistics:")
print(numerical_data_stats)

