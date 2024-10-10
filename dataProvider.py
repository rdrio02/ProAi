import pandas as pd
import streamlit as st

data = pd.read_csv("earthquakes.csv")

st.title("Global Earthquake Data")
st.write("Comprehensive datasets of global earthquake with key attributes for analysis:")
#I have still to write the link to the keggle website
st.write(data.head(5))

st.header("Magnitude")
st.write("Min: ", data["magnitude"].min())
st.write("Min: ", data["magnitude"].mean())
st.write("Min: ", data["magnitude"].max())

st.header("Network")
# This part can be made differently
choosen = st.selectbox("Network :",['us','tx','ci','nn','nc','uu','ak'])
counter = (data["net"].str.contains(choosen)).sum()
st.write(f"The number of earthquakes for {choosen} :", counter)

st.bar_chart(data)