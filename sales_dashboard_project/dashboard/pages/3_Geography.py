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

st.title("🗺️ Geography")

df = pd.read_csv('../data/superstore_cleaned.csv')

state_sales = df.groupby('State')['Sales'].sum().reset_index()
fig = px.choropleth(state_sales, locations="State", locationmode="USA-states", 
                    color="Sales", title="Sales by State", scope="usa")
st.plotly_chart(fig, use_container_width=True)