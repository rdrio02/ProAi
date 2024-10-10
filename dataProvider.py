import pandas as pd
import streamlit as st

data = pd.read_csv("earthquakes.csv")

st.title("Global Earthquake Data")
st.write("Comprehensive datasets of global earthquake with key attributes for analysis:")
#I have still to write the link to the keggle website
st.write(data.head(5))

st.header("Magnitude")
st.write("Min: ", data["magnitude"].min())
st.write("Mean: ", data["magnitude"].mean())
st.write("Max: ", data["magnitude"].max())

st.header("Network")
# This part can be made differently
choosen = st.selectbox("Network :",data['net'].unique())
counter = (data["net"].str.contains(choosen)).sum()
st.write(f"The number of earthquakes for {choosen} :", counter)


subData = data['net'].unique()
subData['numberOfEarthquakes'] = data["net"].unique().sum()

st.bar_chart(subData)
print()