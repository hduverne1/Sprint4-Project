import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('./vehicles_us.csv')

st.header('Car Sales Dashboard')

fig_hist = px.histogram(df, x='price', title='Distribution of Car Prices')
st.plotly_chart(fig_hist)

fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer')
st.plotly_chart(fig_scatter)

if st.checkbox('Show only cars with price less than $20,000'):
    df_filtered = df[df['price'] < 20000]
    fig_filtered = px.scatter(df_filtered, x='odometer', y='price', title='Price vs. Odometer (Filtered)')
    st.plotly_chart(fig_filtered)
