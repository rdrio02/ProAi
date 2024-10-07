import pandas as pd
import streamlit as st

data = pd.read_csv("earthquakes.csv")
print(data)

st.title("Global Earthquake Data")

st.write("Comprehensive datasets of global earthquake with key attributes for analysis:")
#I have still to write the link to the keggle website

st.write(data)
