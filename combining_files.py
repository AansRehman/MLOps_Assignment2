import pandas as pd

# File paths for the CSV files
file1 = 'bbc_scrapper_cleaned.csv'  # Path to the first CSV file
file2 = 'dawn_scrapper_cleaned.csv'  # Path to the second CSV file


df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Drop the existing "ID" column if it already exists
if 'ID' in df1.columns:
    df1 = df1.drop('ID', axis=1)
if 'ID' in df2.columns:
    df2 = df2.drop('ID', axis=1)

# Concatenate the two DataFrames
merged_df = pd.concat([df1, df2], ignore_index=True)

# Add a new ID column with automated numbering
merged_df.insert(0, 'ID', range(1, len(merged_df) + 1))

# Save the new DataFrame to a CSV file
output_path = 'data/merged_data.csv'  # Path for the new CSV file
merged_df.to_csv(output_path, index=False)

# Display the merged DataFrame to check the result
print(merged_df)
