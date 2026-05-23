import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/superstore_cleaned.csv')

# Step 8: Sales by Category
plt.figure(figsize=(10,6))
df.groupby('Category')['Sales'].sum().plot(kind='bar', color='skyblue')
plt.title('Sales by Category')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visuals/sales_by_category.png')
print("Sales by Category chart saved!")

# Step 9: Monthly Sales Trend
monthly = df.groupby('Month')['Sales'].sum().reset_index()
plt.figure(figsize=(12,6))
plt.plot(monthly['Month'], monthly['Sales'], marker='o', color='blue')
plt.title('Monthly Sales Trend')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('visuals/monthly_sales_trend.png')
print("Monthly Sales Trend chart saved!")