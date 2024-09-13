import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Create header
st.header('Vehicle Data Analysis')

# Create and display histogram for the 'price' column
fig_histogram = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_histogram)

# Create and display scatter plot for 'odometer' vs 'price'
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer')
st.plotly_chart(fig_scatter)

# Add checkbox for showing data sample
if st.checkbox('Show Data Sample'):
    # Exclude 'price' column from the sample data
    st.write(df.drop(columns=['price']).sample(10))
