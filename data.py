import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read CSV into DataFrame
df = pd.read_csv("D:/PROJECTS/programs/programs/student performance analytics/student_data.csv")

#clean the dataframe

#convert all invalid entry to NaN
marks_cols = ['Maths', 'English', 'Chemistry','Electronics', 'Python', 'Physics']
lifestyle_cols = ['sleep_hours', 'screen_time']
df[marks_cols + lifestyle_cols] = df[marks_cols + lifestyle_cols].apply(pd.to_numeric, errors='coerce')
# remove rows where ALL subject marks are NaN
df = df.dropna(subset=marks_cols, how='all')
#fill missing values
df[marks_cols] = df[marks_cols].fillna(0)
df['sleep_hours'] = df['sleep_hours'].fillna(df['sleep_hours'].median())
df['screen_time'] = df['screen_time'].fillna(df['screen_time'].median())
#remove duplicate entries
df = df.drop_duplicates(subset=['Student ID'])
# each subject 50 max
df[marks_cols] = df[marks_cols].clip(0, 50)
# Total of all subjects
df['total_marks'] = df[marks_cols].sum(axis=1)
#create section column from student id
# create section column from Student ID
df['section'] = df['Student ID'].str[0]

def search_student():
    try:
        student_id = input("Enter Student ID: ").strip().upper()
        # find student
        student_row = df[df['Student ID'] == student_id]
        if student_row.empty:
            raise ValueError("Student ID not found.")
        student = student_row.iloc[0]
        total = student['total_marks']
        percentage = student['percentage']
        # percentile (relative to all students)
        percentile = (df['percentage'] < percentage).mean() * 100
        # section from ID (A12 → A)
        section = student_id[0]
        print("\n--- Student Details ---")
        print(f"Student ID  : {student_id}")
        print(f"Section     : {section}")
        print(f"Total Marks : {total:.0f} / 300")
        print(f"Percentage  : {percentage:.2f}%")
        print(f"Percentile  : {percentile:.2f}")
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Unexpected error:", e)
