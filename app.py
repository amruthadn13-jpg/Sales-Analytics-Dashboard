import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Sales Analytics Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Use uploaded file or sample file
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Using sample_sales.csv by default")
    df = pd.read_csv("sample_sales.csv")

# Show raw data
st.subheader("Dataset Preview")
st.dataframe(df)

# Basic statistics
st.subheader("Summary Statistics")
st.write(df.describe(include="all"))

# Sidebar filters
st.sidebar.header("Filters")

# Category filter
if "Category" in df.columns:
    categories = df["Category"].unique().tolist()
    selected_categories = st.sidebar.multiselect(
        "Select Categories",
        categories,
        default=categories
    )
    df = df[df["Category"].isin(selected_categories)]

# Region filter
if "Region" in df.columns:
    regions = df["Region"].unique().tolist()
    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        regions,
        default=regions
    )
    df = df[df["Region"].isin(selected_regions)]

# Show filtered data
st.subheader("Filtered Data")
st.dataframe(df)

# KPIs
if "Sales" in df.columns:
    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    max_sales = df["Sales"].max()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"₹{total_sales:,.2f}")
    col2.metric("Average Sale", f"₹{avg_sales:,.2f}")
    col3.metric("Highest Sale", f"₹{max_sales:,.2f}")

# Chart: Sales by Category
if "Category" in df.columns and "Sales" in df.columns:
    st.subheader("Sales by Category")
    category_sales = df.groupby("Category")["Sales"].sum()

    fig, ax = plt.subplots()
    category_sales.plot(kind="bar", ax=ax)
    ax.set_ylabel("Sales")
    st.pyplot(fig)

# Chart: Sales by Region
if "Region" in df.columns and "Sales" in df.columns:
    st.subheader("Sales by Region")
    region_sales = df.groupby("Region")["Sales"].sum()

    fig, ax = plt.subplots()
    region_sales.plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

# Download filtered data
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)
