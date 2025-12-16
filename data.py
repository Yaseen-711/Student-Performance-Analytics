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

# average of 6 subjects, scaled to 100  , Total of all subjects
df['total_marks'] = df[marks_cols].sum(axis=1)



print(df.describe())
print(df.dtypes)