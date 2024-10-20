import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

col1, col2 = st.columns(2)

#Get data from csv files
firstNames = pd.read_csv("first_names.csv")
lastNames = pd.read_csv("last_names.csv")
subjects = pd.read_csv("subjects.csv")

#Creatian of a main table
data = pd.DataFrame(columns=['Student Id', 'Name', 'Subject', 'Grade'])

# This is the first part of the sidebar
with st.sidebar:
    numberStudents = st.number_input("Number of students", min_value = 1, max_value = 1000,value=10, step = 1)
    numberSubjects = st.number_input("Number of subjects", min_value = 1, max_value = 20, value=10, step = 1)
    gradesPerSubject = st.number_input("Grades per subject", min_value = 0, max_value = 6, value=3, step = 1)
    minimumGrade = st.number_input("Minimum grade", min_value = 0, max_value = 60 ,value=0, step = 1)
    maximumGrade = st.number_input("Maximum grade", min_value = 0, max_value = 60 ,value=60, step = 1)


#Get a selection of the subjects
subjects = np.random.choice(subjects.squeeze(), numberSubjects, replace=False)
firstNames = np.random.choice(firstNames.squeeze(), numberStudents, replace=False)
lastNames = np.random.choice(lastNames.squeeze(), numberStudents, replace=False)
lastNames = sorted(lastNames)
names = firstNames + " " + lastNames

# This hole algoritm is resposible to make the hole table by making row per row and apending them into the table
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
            data = pd.concat([data ,pd.DataFrame([newRow])], ignore_index=True)
    counter = counter + 1

# Repairing created col and making a new set of data to be described later
data['Grade'] = pd.to_numeric(data['Grade'], errors='coerce')
data['Student Id'] = pd.to_numeric(data['Student Id'], errors='coerce')
df = data[['Student Id', 'Grade']]

# This is the second part of the sidebar
with st.sidebar:
    selectedStudent = st.selectbox("Select student", data['Name'].unique())


# Creation of histogram using plotly
fig_plotly_histogram = px.histogram(data,
                                    x='Grade',
                                    color='Subject',  # Color by subject
                                    nbins=10,
                                    range_x=[minimumGrade, maximumGrade+1],
                                    title="")

# Create a Matplotlib plot for the selected student's grades
fig, ax = plt.subplots()
ax.hist(data['Grade'], bins=10, color='blue', alpha=0.7, range=(minimumGrade, maximumGrade))
ax.set_title(f"Matplotlib: Grades Distribution for {selectedStudent}")
ax.set_xlabel('Grades')
ax.set_ylabel('Frequency')
st.pyplot(fig)



#Seaborn
fig_seaborn, ax = plt.subplots(figsize=(8, 5))

for subject in data['Subject'].unique():
    subject_data = data[data['Subject'] == subject]  # Filter by subject
    sns.kdeplot(subject_data['Grade'], fill=True, ax=ax, label=subject, clip=(minimumGrade, maximumGrade))

ax.set_title('Seaborn: KDE of Grades by Subject')
ax.set_xlabel('Grades')
ax.set_ylabel('Density')




with col1:
    st.write(data)

    # Display Plotly chart
    st.plotly_chart(fig_plotly_histogram)

    # Show Seaborn plot in Streamlit
    st.pyplot(fig_seaborn)

with col2:
    statistics = df.describe()
    st.write(statistics)