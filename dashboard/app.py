import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide")

# Deep Dark Theme
st.markdown("""
    <style>
    .main, .stApp {background-color: #0A0A0A !important;}
    .stSidebar {background-color: #111111 !important;}
    h1, h2, h3, p, label, .stMetricLabel {color: #FFFFFF !important; font-weight: bold !important;}
    .stMetricValue {color: #00FFAA !important; font-weight: bold !important;}
    </style>
    """, unsafe_allow_html=True)

# Correct Path
import os

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, '..', 'data', 'superstore_cleaned.csv')

df = pd.read_csv(csv_path)
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

st.title("🛒 Superstore Sales Analytics Dashboard")
st.markdown("**Advanced Dashboard** - Hielite Academy (Oni Temidare David)")

# KPIs
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
col3.metric("Total Orders", f"{df['Order ID'].nunique():,}")
col4.metric("Avg Sales/Order", f"${df['Sales'].mean():.2f}")
col5.metric("Profit Margin", f"{(df['Profit'].sum()/df['Sales'].sum()*100):.1f}%")

# Sidebar Filters
st.sidebar.header("🔍 Filters")

selected_region = st.sidebar.multiselect("Select Region(s)", options=sorted(df['Region'].unique()), default=df['Region'].unique(), help="Type to search")

selected_category = st.sidebar.multiselect("Select Category", df['Category'].unique(), default=df['Category'].unique())

if selected_category:
    available_sub = sorted(df[df['Category'].isin(selected_category)]['Sub-Category'].unique())
else:
    available_sub = sorted(df['Sub-Category'].unique())
selected_subcategory = st.sidebar.multiselect("Select Sub-Category", available_sub, default=[])

selected_segment = st.sidebar.multiselect("Select Segment", df['Segment'].unique(), default=df['Segment'].unique())

min_date = df['Order Date'].min()
max_date = df['Order Date'].max()
date_range = st.sidebar.date_input("Date Range", [min_date, max_date])

# Filter Data
filtered_df = df[
    (df['Region'].isin(selected_region)) &
    (df['Category'].isin(selected_category)) &
    (df['Segment'].isin(selected_segment)) &
    (df['Order Date'].dt.date.between(date_range[0], date_range[1]))
]

if selected_subcategory:
    filtered_df = filtered_df[filtered_df['Sub-Category'].isin(selected_subcategory)]

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Overview", "Trends", "Geography", "Top Products", "Discount", "Shipping"])

with tab1:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.plotly_chart(px.bar(filtered_df.groupby('Category')['Sales'].sum().reset_index(), x='Category', y='Sales', title="Sales by Category", color='Category'), use_container_width=True)
    with c2:
        st.plotly_chart(px.pie(filtered_df, names='Segment', values='Sales', title="Sales by Segment"), use_container_width=True)
    with c3:
        st.plotly_chart(px.bar(filtered_df.groupby('Segment')['Profit'].sum().reset_index(), x='Segment', y='Profit', title="Profit by Segment", color='Segment'), use_container_width=True)

with tab2:
    monthly = filtered_df.groupby('Month')[['Sales', 'Profit']].sum().reset_index()
    st.plotly_chart(px.line(monthly, x='Month', y=['Sales', 'Profit'], title="Monthly Sales & Profit Trend", markers=True), use_container_width=True)

with tab3:
    state_sales = filtered_df.groupby('State')['Sales'].sum().reset_index()
    fig = px.choropleth(state_sales, locations="State", locationmode="USA-states", color="Sales", title="Sales by State", scope="usa")
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    c1, c2 = st.columns(2)
    with c1:
        top_sales = filtered_df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()
        st.plotly_chart(px.bar(top_sales, x='Sales', y='Product Name', orientation='h', title="Top 10 by Sales"), use_container_width=True)
    with c2:
        top_profit = filtered_df.groupby('Product Name')['Profit'].sum().nlargest(10).reset_index()
        st.plotly_chart(px.bar(top_profit, x='Profit', y='Product Name', orientation='h', title="Top 10 by Profit"), use_container_width=True)

with tab5:
    st.plotly_chart(px.scatter(filtered_df, x='Discount', y='Profit', color='Category', hover_data=['Product Name', 'Sales'], title="Discount Impact on Profit"), use_container_width=True)

with tab6:
    shipping = filtered_df.groupby('Ship Mode')['Shipping Days'].mean().reset_index()
    st.plotly_chart(px.bar(shipping, x='Ship Mode', y='Shipping Days', title="Average Shipping Days by Ship Mode"), use_container_width=True)

# Download
csv = filtered_df.to_csv(index=False)
st.download_button("📥 Download Filtered Data", csv, "filtered_sales_data.csv", "text/csv")

st.caption("Hielite Academy - Advanced Sales Dashboard | Oni Temidare David")