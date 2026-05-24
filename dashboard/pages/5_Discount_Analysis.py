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

st.title("📉 Discount Analysis")

import os
df = pd.read_csv('../data/superstore_cleaned.csv')

st.plotly_chart(px.scatter(df, x='Discount', y='Profit', color='Category', 
                           hover_data=['Product Name', 'Sales'], title="Discount Impact on Profit"), 
                use_container_width=True)