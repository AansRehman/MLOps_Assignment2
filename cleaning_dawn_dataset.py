import pandas as pd

# Function to clean data and add ID at the start of each row
def clean_and_add_id(input_csv, output_csv):
    # Read the data from the CSV file
    df = pd.read_csv(input_csv)

    # Remove rows with no title or empty title
    df_cleaned = df[df['Title'].notna() & (df['Title'].str.strip() != '')]

    # Add an auto-incremented ID column
    df_cleaned['ID'] = range(1, len(df_cleaned) + 1)

    # Reorder the columns to place 'ID' at the beginning
    columns_order = ['ID'] + [col for col in df_cleaned.columns if col != 'ID']
    df_cleaned = df_cleaned[columns_order]

    # Save the cleaned data to a new CSV file
    df_cleaned.to_csv(output_csv, index=False)

    return df_cleaned  # Return the cleaned DataFrame


# Path to the existing CSV file
input_csv = 'dawn_scrapper.csv'

# Path to the new cleaned CSV file
output_csv = 'dawn_scrapper_cleaned.csv'

# Clean the data and add an auto-incremented ID at the start
cleaned_df = clean_and_add_id(input_csv, output_csv)

# Display the cleaned DataFrame
print(cleaned_df)
