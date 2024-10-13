import streamlit as st
import pandas as pd

dataURL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columnNames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(dataURL, header=None, names=columnNames)

st.title("Iris Data")
st.write("Here are the first 5 data rows")
st.write(df.head(5))


st.write("There are some basic statistics: ")
statistics = df.describe()
st.write(statistics)

st.header("Data distribution")


for i in range(1, 5):
    st.bar_chart(subData.set_index(i))





