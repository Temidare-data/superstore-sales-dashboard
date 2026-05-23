import pandas as pd

print("=== STEP 6: DATA CLEANING ===")

df = pd.read_csv('data/superstore.csv', encoding='latin1')

print("Original Shape:", df.shape)

# Super flexible date conversion
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# Create new columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()
df['Profit Margin'] = (df['Profit'] / df['Sales'] * 100).round(2)

# Remove duplicates
df = df.drop_duplicates()

# Save
df.to_csv('data/superstore_cleaned.csv', index=False)

print("✅ CLEANING COMPLETED!")
print("New Shape:", df.shape)
print("\nFirst 5 Order Dates:")
print(df[['Order Date', 'Year', 'Month']].head())
print("\nProfit column exists:", 'Profit' in df.columns)