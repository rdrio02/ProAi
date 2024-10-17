import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib as plt
#import seaborn as sb
import random


col1, col2 = st.columns(2)
with st.sidebar:
    numberStudents = st.number_input("Number of students", min_value = 1, max_value = 45,value=10, step = 1)
    numberSubjects = st.number_input("Number of subjects", min_value = 1, max_value = 20, value=10, step = 1)
    gradesPerSubject = st.number_input("Grades per subject", min_value = 0, max_value = 6, value=3, step = 1)
    minimumGrade = st.number_input("Minimum grade", min_value = 0, max_value = 60 ,value=30, step = 1)
    maximumGrade = st.number_input("Maximum grade", min_value = 0, max_value = 60 ,value=30, step = 1)
#    selectedStudent = st.selectbox("Select student", df['Student name'].unique())


#Get data from csv files
firstNames = pd.read_csv("first_names.csv")
lastNames = pd.read_csv("last_names.csv")
subjects = pd.read_csv("subjects.csv")

#Make dataBase
data = ['ID', 'Name', 'Subject', 'Grade']

#Get a selection of the subjects
subjects = np.random.choice(subjects.squeeze(), numberSubjects, replace=False)
firstNames = np.random.choice(firstNames.squeeze(), numberStudents, replace=False)
lastNames = np.random.choice(lastNames.squeeze(), numberStudents, replace=False)
lastNames = sorted(lastNames)
names = firstNames + " " + lastNames

counter = 0
for name in names:
    for  subject in subjects:
        for i in range(gradesPerSubject):
            newRow = {
                "ID": counter,
                "Name": name,
                "Subject": subject,
                "Grade": np.random.randint(minimumGrade, maximumGrade)
            }
            #newRow = {"ID" : counter, "Name" : name, "Subject" : subject, "Grade" : random.randint(minimumGrade,maximumGrade+1)}
            data = data.append(newRow, ignore_index=True)
    counter = counter + 1

st.write(data)


with col1:
    st.write("s")

with col2:
    st.write("h")