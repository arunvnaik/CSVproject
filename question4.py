import pandas as pd

# Load the dataset, skipping bad lines
df = pd.read_csv('https://docs.google.com/spreadsheets/d/1FXmmFDS0r6SNE1ZPizrwYjNRC4ZgnCC_M4WcNCVGp0U/export?format=csv', on_bad_lines='skip')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check the column names
print("Column names:", df.columns)

# Ensure that the column 'Rate' exists before dropping it
if 'Rate' in df.columns:
    # Drop the 'Rate' column
    df = df.drop('Rate', axis=1)
    print("Column 'Rate' dropped successfully.")
else:
    print("Column 'Rate' not found.")

# Now, you can continue with your analysis or operations on the dataframe
