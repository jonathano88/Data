import pandas as pd
path='C:\\Users\\jonat\\OneDrive - Whitecliffe College\\IT9115 Project\\Data\\CSV\\'
# Read CSV files\
df_A = pd.read_csv(path+'dataset_20241023.csv')
df_B = pd.read_csv(path+'dataset_20241028.csv')
df_C = pd.read_csv(path+'dataset_20241029.csv')


# Set the ID field as the index
df_A.set_index('id', inplace=True)
df_B.set_index('id', inplace=True)
df_C.set_index('id', inplace=True)

# Combine the DataFrames, giving priority to df_B
merged_df = df_B.combine_first(df_A).reset_index()
merged_df = df_C.combine_first(merged_df).reset_index()

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(path+'dataset_merged2.csv', index=False)
