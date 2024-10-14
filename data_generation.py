import streamlit as st
import pandas as pd
#import numpy as np
#import matplotlib as plt
#import seaborn as sb

firstNames = pd.read_csv("first_names.csv")
lastNames = pd.read_csv("last_names.csv")
subjects = pd.read_csv("subjects.csv")


df = []

col1, col2 = st.columns(2)
with st.sidebar:
    numberStudents = st.number_input("Number of students")
    numberSubjects = st.number_input("Number of subjects")
    gradesPerSubject = st.number_input("Grades per subject")
    minimumGrade = st.number_input("Minimum grade")
    maximumGrade = st.number_input("Maximum grade")
    selectedStudent = st.selectbox("Select student", df['Student'].unique())




with col1:
    st.write("s")

with col2:
    st.write("h")