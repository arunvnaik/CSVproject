import pandas as pd

# Load the dataset, skipping bad lines
df = pd.read_csv('https://docs.google.com/spreadsheets/d/1FXmmFDS0r6SNE1ZPizrwYjNRC4ZgnCC_M4WcNCVGp0U/export?format=csv', on_bad_lines='skip')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Generate summary statistics for numerical columns
print("\nSummary statistics for numerical columns:")
numerical_summary = df.describe()
print(numerical_summary)

# Generate summary statistics for categorical columns
print("\nSummary statistics for categorical columns:")
categorical_summary = df.describe(include=['object'])
print(categorical_summary)

# Provide insights on data distributions
print("\nData distribution insights:")
for column in df.select_dtypes(include=['object']).columns:
    print(f"\nDistribution for categorical column '{column}':")
    print(df[column].value_counts())
