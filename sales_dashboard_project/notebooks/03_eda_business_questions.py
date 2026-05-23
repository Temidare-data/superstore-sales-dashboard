import pandas as pd

print("=== STEP 7: EXPLORATORY DATA ANALYSIS & BUSINESS QUESTIONS ===")

df = pd.read_csv('data/superstore_cleaned.csv')

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()

print("Total Sales     :", "${:,.2f}".format(total_sales))
print("Total Profit    :", "${:,.2f}".format(total_profit))
print("Total Orders    :", total_orders)
print("Profit Margin   :", "{:.2f}%".format((total_profit / total_sales * 100)))

print("\n1. Which category generates the highest sales?")
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))

print("\n2. Which region is most profitable?")
print(df.groupby('Region')['Profit'].sum().sort_values(ascending=False))

print("\n3. Top 10 Best Selling Products:")
print(df.groupby('Product Name')['Sales'].sum().nlargest(10))