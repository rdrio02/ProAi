import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib as plt
#import seaborn as sb
import random

#Get data from csv files
firstNames = pd.read_csv("first_names.csv")
lastNames = pd.read_csv("last_names.csv")
subjects = pd.read_csv("subjects.csv")

#Creation of a main table
mainTable = pd.DataFrame(columns=['Student Id', 'Name', 'Subject', 'Grade'])

#Get all the values needed to make up all the students and there grades per subject
with st.sidebar:
    numberStudents = st.number_input("Number of students", min_value = 1, max_value = 45,value=10, step = 1)
    numberSubjects = st.number_input("Number of subjects", min_value = 1, max_value = 20, value=10, step = 1)
    gradesPerSubject = st.number_input("Grades per subject", min_value = 0, max_value = 6, value=3, step = 1)
    minimumGrade = st.number_input("Minimum grade", min_value = 0, max_value = 60 ,value=30, step = 1)
    maximumGrade = st.number_input("Maximum grade", min_value = 0, max_value = 60 ,value=30, step = 1)

#Make all the list needed with information as Name, subject an ... , to give to the main Table afterwards
subjects = np.random.choice(subjects.squeeze(), numberSubjects, replace=False)
firstNames = np.random.choice(firstNames.squeeze(), numberStudents, replace=False)
lastNames = np.random.choice(lastNames.squeeze(), numberStudents, replace=False)
lastNames = sorted(lastNames)
names = firstNames + " " + lastNames

#This part of the code is responsible to make all the data with goes into the mainTable by making row to row and concat each row into the mainTable
counter = 1
for name in names:
    for  subject in subjects:
        for i in range(gradesPerSubject):
            newRow = {
                "Student Id": counter,
                "Name": name,
                "Subject": subject,
                "Grade": random.randint(minimumGrade, maximumGrade)
            }
            mainTable = pd.concat([mainTable ,pd.dataFrame([newRow])], ignore_index=True)
    counter = counter + 1


mainTable['Grade'] = pd.to_numeric(mainTable['Grade'], errors='coerce')
mainTable['Student Id'] = pd.to_numeric(mainTable['Student Id'], errors='coerce')
df = mainTable[['Student Id', 'Grade']]


with st.sidebar:
    selectedStudent = st.selectbox("Select student", mainTable['Name'].unique())


with col1:
    st.write(mainTable)

with col2:
    statistics = df.describe()
    st.write(statistics)