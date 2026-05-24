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

st.title("📈 Trends")

import os
df = pd.read_csv('../data/superstore_cleaned.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

monthly = df.groupby('Month')[['Sales', 'Profit']].sum().reset_index()
st.plotly_chart(px.line(monthly, x='Month', y=['Sales', 'Profit'], 
                        title="Monthly Sales & Profit Trend", markers=True), use_container_width=True)