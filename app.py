import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('./vehicles_us.csv')

# Header
st.header('US Vehicle Advertisement Listings')

# Brand selection
brands = df['model'].unique()
selected_brands = st.multiselect('Select car brands to view data', brands)

if selected_brands:
    df = df[df['model'].isin(selected_brands)]

# Distribution of Prices by Car Brand
fig_price_distribution = px.box(df, x='model', y='price', title='Distribution of Prices by Car Brand')
st.plotly_chart(fig_price_distribution)

# Number of Days Listed for Sale by Car Brand
fig_days_listed = px.bar(df, x='model', y='days_listed', title='Number of Days Listed for Sale by Car Brand')
st.plotly_chart(fig_days_listed)
# Type of Vehicles by Car Brand
fig_vehicle_type = px.bar(df, x='model', color='type', title='Type of Vehicles by Car Brand', barmode='group')
st.plotly_chart(fig_vehicle_type)

# Odometer Reading vs Price
fig_scatter = px.scatter(df, x='odometer', y='price', title='Odometer Reading vs Price')
st.plotly_chart(fig_scatter)

# Number of Days Listed for Sale vs Price
fig_days_vs_price = px.scatter(df, x='days_listed', y='price', title='Number of Days Listed for Sale vs Price')
st.plotly_chart(fig_days_vs_price)

# Checkbox to filter by price
if st.checkbox('Show only cars with price less than $20,000'):
    df_filtered = df[df['price'] < 20000]
    fig_filtered = px.scatter(df_filtered, x='odometer', y='price', title='Price vs. Odometer (Filtered)')
    st.plotly_chart(fig_filtered)