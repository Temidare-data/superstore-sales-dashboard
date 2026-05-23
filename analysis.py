import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/superstore_cleaned.csv')

print("=== BUSINESS QUESTIONS ANSWERS ===\n")

# 1. Total Sales and Profit
total_sales = df['Sales'].sum()
print(f"Total Sales: ${total_sales:,.2f}")

# 2. Highest Sales Category
print("\nCategory with Highest Sales:")
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))

# 3. Most Profitable Region (Note: No Profit column, using Sales instead)
print("\nRegion with Highest Sales:")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

# 4. Monthly Sales Trend
monthly = df.groupby('Month')['Sales'].sum()
print("\nMonthly Sales Trend:")
print(monthly.sort_values(ascending=False))

# 5. Top Products
print("\nTop 5 Best Selling Products:")
print(df.groupby('Product Name')['Sales'].sum().nlargest(5))