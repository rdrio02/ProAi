import pandas as pd
import streamlit as st

data = pd.read_csv("earthquakes.csv")

st.header("Global Earthquake Data")
st.write("Comprehensive datasets of global earthquake with key attributes for analysis:")
#I have still to write the link to the keggle website
st.write(data.head(5))
st.subheader("Magnitude")
st.write("Min: ", data.iloc[3].min())