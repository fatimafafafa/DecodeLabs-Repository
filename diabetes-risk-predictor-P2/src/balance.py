import pandas as pd
from sklearn.utils import resample

# Load dataset
df = pd.read_csv("../data/diabetes_cleaned.csv")

non_diabetic = df[df["Outcome"] == 0]
diabetic = df[df["Outcome"] == 1]

non_diabetic_balanced = resample(
    non_diabetic,
    replace=False,
    n_samples=len(diabetic),
    random_state=42
)

# Combine & shuffle
balanced_df = pd.concat([non_diabetic_balanced, diabetic])
balanced_df = balanced_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to new CSV in data folder
output_path = "../data/diabetes_balanced.csv"
balanced_df.to_csv(output_path, index=False)

print("Saved balanced dataset to:", output_path)
print("\nClass distribution:")
print(balanced_df["Outcome"].value_counts())