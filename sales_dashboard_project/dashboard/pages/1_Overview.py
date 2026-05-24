import streamlit as st
import pandas as pd
import plotly.express as px

# Strong Dark Theme + Visible Sidebar
st.markdown("""
    <style>
    .main, .stApp {background-color: #0A0A0A !important;}
    .stSidebar {background-color: #1A1A1A !important; border-right: 3px solid #00FFAA !important;}
    h1, h2, h3, p, label, .stMetricLabel {color: #FFFFFF !important; font-weight: bold !important;}
    .stMetricValue {color: #00FFAA !important; font-weight: bold !important; font-size: 28px !important;}
    .stMultiSelect label, .stDateInput label {color: #FFFFFF !important; font-weight: bold !important;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("**Advanced Dashboard** - Hielite Academy (Oni Temidare David)")

st.title("📊 Overview")

df = pd.read_csv('../data/superstore_cleaned.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# KPIs
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
col3.metric("Total Orders", f"{df['Order ID'].nunique():,}")
col4.metric("Avg Sales/Order", f"${df['Sales'].mean():.2f}")
col5.metric("Profit Margin", f"{(df['Profit'].sum()/df['Sales'].sum()*100):.1f}%")

# Charts
c1, c2, c3 = st.columns(3)
with c1:
    st.plotly_chart(px.bar(df.groupby('Category')['Sales'].sum().reset_index(), x='Category', y='Sales', title="Sales by Category", color='Category'), use_container_width=True)
with c2:
    st.plotly_chart(px.pie(df, names='Segment', values='Sales', title="Sales by Segment"), use_container_width=True)
with c3:
    st.plotly_chart(px.bar(df.groupby('Segment')['Profit'].sum().reset_index(), x='Segment', y='Profit', title="Profit by Segment", color='Segment'), use_container_width=True)