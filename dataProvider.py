import pandas as pd
import streamlit as st

data = pd.read_csv("earthquakes.csv")

st.title("Global Earthquake Data")
st.write("Comprehensive datasets of global earthquake with key attributes for analysis:")
#I have still to write the link to the keggle website
st.write(data.head(5))

st.subheader("Magnitude")
st.write("Min: ", data["magnitude"].min())
st.write("Min: ", data["magnitude"].mean())
st.write("Min: ", data["magnitude"].max())

st.subheader("Network")
st.write("Network :")
# This part can be made differently
choosen = st.multiselect("",['us','tx','ci','nn','nc','uu','ak'])
counter = (data["net"] == choosen).sum()
st.write(f"The number of earthquakes for {choosen} :", counter)