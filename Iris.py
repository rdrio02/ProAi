import streamlit as st
import pandas as pd

dataURL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columnNames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(data_url, header=None, names=column_names)

st.title("Iris Data")
st.write("Here are the first 5 data rows")
st.write(df.head(5))



