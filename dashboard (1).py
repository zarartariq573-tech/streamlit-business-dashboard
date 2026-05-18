import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Business Dashboard",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_excel("Global_Superstore2.xlsx")

# -----------------------------
# Data Cleaning
# -----------------------------
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df['Order Date'] = pd.to_datetime(df['Order Date'])

# -----------------------------
# Dashboard Title
# -----------------------------
st.title("Interactive Business Dashboard")

st.markdown("### Sales, Profit and Customer Analysis")

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filter Data")

# Region Filter
region = st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

# Category Filter
category = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

# Sub-Category Filter
sub_category = st.sidebar.multiselect(
    "Select Sub-Category",
    options=df['Sub-Category'].unique(),
    default=df['Sub-Category'].unique()
)

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Sub-Category'].isin(sub_category))
]

# -----------------------------
# KPIs
# -----------------------------
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()

top_customers = (
    filtered_df.groupby('Customer Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

# -----------------------------
# KPI Display
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", f"${total_sales:,.2f}")

with col2:
    st.metric("Total Profit", f"${total_profit:,.2f}")

# -----------------------------
# Sales by Category Chart
# -----------------------------
sales_chart = px.bar(
    filtered_df,
    x='Category',
    y='Sales',
    color='Category',
    title='Sales by Category'
)

st.plotly_chart(sales_chart, use_container_width=True)

# -----------------------------
# Profit by Region Chart
# -----------------------------
profit_chart = px.pie(
    filtered_df,
    names='Region',
    values='Profit',
    title='Profit by Region'
)

st.plotly_chart(profit_chart, use_container_width=True)

# -----------------------------
# Top 5 Customers Chart
# -----------------------------
top_customer_chart = px.bar(
    top_customers,
    x='Customer Name',
    y='Sales',
    color='Sales',
    title='Top 5 Customers by Sales'
)

st.plotly_chart(top_customer_chart, use_container_width=True)

# -----------------------------
# Show Data
# -----------------------------
st.subheader("Filtered Dataset")

st.dataframe(filtered_df)
