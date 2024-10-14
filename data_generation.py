import streamlit as st
import pandas as pd
#import numpy as np
#import matplotlib as plt
#import seaborn as sb

firstNames = pd.read_csv("first_names.csv")
lastNames = pd.read_csv("last_names.csv")
subjects = pd.read_csv("subjects.csv")

col1, col2 = st.columns(2)

with st.sidebar:
    st.write("hello")

with col1:
    st.write("a cat")
    st.write("pp")

with col2:
    st.write("a red cat")