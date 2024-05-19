import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Data Visualization

# Histogram for numerical columns
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Boxplot for numerical columns
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot of {column}')
    plt.xlabel(column)
    plt.grid(True)
    plt.show()

# Bar plot for categorical columns
for column in df.select_dtypes(include=['object']).columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(y=df[column], order=df[column].value_counts().index)
    plt.title(f'Bar plot of {column}')
    plt.xlabel('Count')
    plt.ylabel(column)
    plt.grid(True)
    plt.show()
