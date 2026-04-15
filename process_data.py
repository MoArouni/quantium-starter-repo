import pandas as pd
import os

# 1. Define paths
data_folder = './data'
output_file = 'formatted_data.csv'

# This list will hold the processed data from each file
processed_dataframes = []

# 2. Loop through the three CSV files in the data folder
for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder, filename)
        
        # Load the current CSV
        df = pd.read_csv(file_path)
        
        # 3. Filter for "pink morsel" only
        df = df[df['product'].str.lower() == 'pink morsel']
        
        # 4. Clean the "price" column (remove '$' and convert to float)
        df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
        
        # 5. Calculate "sales" (price * quantity)
        df['sales'] = df['price'] * df['quantity']
        
        # 6. Keep only the requested columns
        df = df[['sales', 'date', 'region']]
        
        processed_dataframes.append(df)

# 7. Combine all three files into one
final_df = pd.concat(processed_dataframes, ignore_index=True)

# 8. Rename columns to match the task's capitalization (Sales, Date, Region)
final_df.columns = ['Sales', 'Date', 'Region']

# 9. Save to a single CSV file
final_df.to_csv(output_file, index=False)

print(f"Success! {output_file} has been created.")