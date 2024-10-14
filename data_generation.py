import streamlit as st
import pandas as pd
#import numpy as np
#import matplotlib as plt
#import seaborn as sb

firstNames = pd.read_csv("first_names.csv")
lastNames = pd.read_csv("last_names.csv")
subjects = pd.read_csv("subjects.csv")

@st.fragment
def fragment_function():
    st.write("Hello")