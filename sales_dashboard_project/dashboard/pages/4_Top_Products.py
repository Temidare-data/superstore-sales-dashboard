import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
    <style>
    .main, .stApp {background-color: #0A0A0A !important;}
    .stSidebar {background-color: #1A1A1A !important; border-right: 3px solid #00FFAA;}
    h1, h2, h3, p, label {color: #FFFFFF !important; font-weight: bold !important;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("**Advanced Dashboard** - Hielite Academy (Oni Temidare David)")

st.title("🔝 Top Products")

df = pd.read_csv('../data/superstore_cleaned.csv')

c1, c2 = st.columns(2)
with c1:
    top_sales = df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()
    st.plotly_chart(px.bar(top_sales, x='Sales', y='Product Name', orientation='h', title="Top 10 by Sales"), use_container_width=True)
with c2:
    top_profit = df.groupby('Product Name')['Profit'].sum().nlargest(10).reset_index()
    st.plotly_chart(px.bar(top_profit, x='Profit', y='Product Name', orientation='h', title="Top 10 by Profit"), use_container_width=True)