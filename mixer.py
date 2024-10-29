import pandas as pd

# Read CSV files\
df_A = pd.read_csv('C:\\Users\\jonat\\OneDrive - Whitecliffe College\\IT9115 Project\\Data\\dataset_20240907_plusP.csv')
df_B = pd.read_csv('C:\\Users\\jonat\\OneDrive - Whitecliffe College\\IT9115 Project\\Data\\dataset_20241023_plusP.csv')

# Set the ID field as the index
df_A.set_index('id', inplace=True)
df_B.set_index('id', inplace=True)

# Combine the DataFrames, giving priority to df_B
merged_df = df_B.combine_first(df_A).reset_index()

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('C:\\Users\\jonat\\OneDrive - Whitecliffe College\\IT9115 Project\\Data\\dataset_merged_plusP.csv', index=False)