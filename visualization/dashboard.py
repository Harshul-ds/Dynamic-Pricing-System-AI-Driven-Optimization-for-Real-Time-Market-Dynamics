import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Dynamic Pricing Dashboard")

# Sidebar
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("## Data Preview")
    st.write(data.head())

    st.write("## Price Trends")
    fig = px.line(data, x="date", y="price", title="Price Trends Over Time")
    st.plotly_chart(fig)
