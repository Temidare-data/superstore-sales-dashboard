import pandas as pd
import plotly.express as px

df = pd.read_csv('data/superstore_cleaned.csv')

print("=== STEP 10: INTERACTIVE PLOTLY CHARTS ===")

fig1 = px.bar(df.groupby('Category')['Sales'].sum().reset_index(), 
              x='Category', y='Sales', title='Sales by Category', color='Category')
fig1.show()

fig2 = px.pie(df, names='Region', values='Profit', title='Profit by Region')
fig2.show()

monthly = df.groupby('Month')[['Sales', 'Profit']].sum().reset_index()
fig3 = px.line(monthly, x='Month', y=['Sales', 'Profit'], title='Monthly Sales & Profit Trend', markers=True)
fig3.show()