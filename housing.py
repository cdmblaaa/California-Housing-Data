import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')

st.title('California Housing Data(1990)by Xinrui Pan')
df = pd.read_csv('housing.csv')



price_filter = st.slider('Median House Price:', 0.0, 500001.0, 200000.0)


st.subheader('See more filters in the sidebar')
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults




level = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Median', 'High'))


if level == 'Low':
   df = df[df.median_income <= 2.5]
elif level =='High':
   df = df[df.median_income > 4.5]
else:
   df = df[df.median_income >2.5]


df = df[df.ocean_proximity.isin(location_filter)]
df = df[df.median_house_value >= price_filter]


st.map(df)


# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots()
ax.hist(df.median_house_value,bins = 30)
plt.xlim =([ 0, price_filter])
st.pyplot(fig)







