import pandas as pd

# Load the two CSV files into pandas DataFrames

file1 = 'Book1.csv'
file2 = 'Book2.csv'
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Merge the two DataFrames
merged_df = pd.concat([df1, df2], ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_file = 'Book.csv'
merged_df.to_csv(merged_file, index=False)
print("Merged CSV file saved as:", merged_file)
