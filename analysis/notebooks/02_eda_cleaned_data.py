import pandas as pd

#Reading in data
cleaned_data_path = '../data/processed/cleaned_feedzai_full.csv'
cleaned_data = pd.read_csv(cleaned_data_path)

#looking at data
print(cleaned_data.head().T)
print(cleaned_data.describe().T)

#Bias Checking
income_bias_check = cleaned_data.groupby('fraud_bool')['num__income'].mean()
age_bias_check = cleaned_data.groupby('fraud_bool')['customer_age'].mean()
credit_bias_check = cleaned_data.groupby('fraud_bool')['credit_risk_score'].mean()
employment_fraud = pd.crosstab(cleaned_data['employment_status'], cleaned_data['fraud_bool'])
housing_status = pd.crosstab(cleaned_data['housing_status'], cleaned_data['fraud_bool'])
payment_type = pd.crosstab(cleaned_data['payment_type'], cleaned_data['fraud_bool'])
has_other_cards = pd.crosstab(cleaned_data['has_other_cards'], cleaned_data['fraud_bool'])
foreign_request = pd.crosstab(cleaned_data['foreign_request'], cleaned_data['fraud_bool'])

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

numerical_data_stats = cleaned_data[['customer_age', 'credit_risk_score','income', 'has_other_cards', 'foreign_request', 'employment_status','housing_status', 'payment_type']].agg(['mean', 'median', 'var', 'skew'])
print("\nNumerical Statistics:")
print(numerical_data_stats)