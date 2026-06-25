import pandas as pd

# Load dataset
df = pd.read_csv("../data/diabetes_cleaned.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nOutcome distribution:")
print(df["Outcome"].value_counts())

print("\nBasic statistics:")
print(df.describe())
columns_with_possible_zero_errors = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

print("\nZero values in important medical columns:")
for col in columns_with_possible_zero_errors:
    print(col, ":", (df[col] == 0).sum())

for col in columns_with_possible_zero_errors:
    median_value = df[col].median()
    df[col] = df[col].replace(0, median_value)

print("\nZero values after cleaning:")
for col in columns_with_possible_zero_errors:
    print(col, ":", (df[col] == 0).sum()) 
df.to_csv("../data/diabetes_cleaned.csv", index=False)

print("\nCleaned dataset saved as diabetes_cleaned.csv")       