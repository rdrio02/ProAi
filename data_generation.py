import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib as plt
#import seaborn as sb



col1, col2 = st.columns(2)
with st.sidebar:
    numberStudents = st.number_input("Number of students", min_value = 1, max_value = 45,value=10, step = 1)
    numberSubjects = st.number_input("Number of subjects", min_value = 1, max_value = 20, value=10, step = 1)
    gradesPerSubject = st.number_input("Grades per subject", min_value = 0, max_value = 6, value=3, step = 1)
    minimumGrade = st.number_input("Minimum grade", min_value = 0, max_value = 60 ,value=30, step = 1)
    maximumGrade = st.number_input("Maximum grade", min_value = 0, max_value = 60 ,value=30, step = 1)
#    selectedStudent = st.selectbox("Select student", df['Student name'].unique())



firstNames = pd.read_csv("first_names.csv")
lastNames = pd.read_csv("last_names.csv")
subjects = pd.read_csv("subjects.csv")

#Get a selection of the subjects
selectedSubjects = np.random.choice(subjects.squeeze(), numberSubjects, replace=False)
selectedFirstNames = np.random.choice(firstNames.squeeze(), numberStudents, replace=False)
selectedLastNames = np.random.choice(lastNames.squeeze(), numberStudents, replace=False)
selectedLastNames.sort_values()
st.write(selectedFirstNames)
st.write(selectedLastNames)





with col1:
    st.write("s")

with col2:
    st.write("h")