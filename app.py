import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Ensure 'price' column is numeric and handle missing or incorrect data
df['price'] = pd.to_numeric(df['price'], errors='coerce')  # Coerce non-numeric to NaN
df = df.dropna(subset=['price'])  # Drop rows with NaN in 'price'
df['price'] = df['price'].astype('int64')  # Convert 'price' to int64

# Streamlit header
st.header('Vehicle Data Analysis')

# Plotly histogram for price distribution
fig_histogram = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_histogram)

# Scatter plot for price vs odometer
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer')
st.plotly_chart(fig_scatter)

# Checkbox to show a data sample
if st.checkbox('Show Data Sample'):
    st.write(df.sample(10))

