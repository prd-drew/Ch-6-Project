import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('vehicles_us.csv')
st.header('Vehicle Data Analysis')
fig_histogram = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_histogram)
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer')
st.plotly_chart(fig_scatter)
if st.checkbox('Show Data Sample'):
    st.write(df.sample(10))
