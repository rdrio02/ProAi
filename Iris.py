import streamlit as st
import pandas as pd

dataURL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columnNames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(dataURL, header=None, names=columnNames)

st.title("Iris Data")
st.write("Here are the first 5 data rows")
st.write(df.head(5))

st.write("Here are some basic information about the database.")

basicStats = ["", 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
functions = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
basicStats[""] = functions
st.write(basicStats)
for