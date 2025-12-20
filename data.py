import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read CSV into DataFrame
df = pd.read_csv("D:/PROJECTS/programs/programs/student performance analytics/student_data.csv")

#columns
marks_cols = ['Maths', 'English', 'Chemistry','Electronics', 'Python', 'Physics']
lifestyle_cols = ['sleep_hours', 'screen_time']

#convert all invalid entry to NaN
df[marks_cols + lifestyle_cols] = df[marks_cols + lifestyle_cols].apply(pd.to_numeric, errors='coerce')
# remove rows where ALL subject marks are NaN
df = df.dropna(subset=marks_cols, how='all')
#fill missing values
df[marks_cols] = df[marks_cols].fillna(0)
df['sleep_hours'] = df['sleep_hours'].fillna(df['sleep_hours'].median())
df['screen_time'] = df['screen_time'].fillna(df['screen_time'].median())
#remove duplicate entries
df = df.drop_duplicates(subset=['Student ID'])
# limit each subject 50 max
df[marks_cols] = df[marks_cols].clip(0, 50)
#something
df['gender'] = df['gender'].str.strip().str.lower()
df['gender'] = df['gender'].replace({'female': 'f', 'male': 'm'})
# Add Total of all subjects and percentage 
df['total_marks'] = df[marks_cols].sum(axis=1)
df['percentage'] = (df['total_marks'] / 300) * 100
# Create section column from Student ID
df['section'] = df['Student ID'].str[0]

#1. Search student
def search_student():
    try:
        sid = input("Enter Student ID: ").strip().upper()
        row = df[df['Student ID'] == sid]
        if row.empty:
            print("Student ID not found")
            return
        s = row.iloc[0]
        pct = s['percentage']
        rank = (df['percentage'] > pct).sum() + 1
        percentile = rank / len(df) * 100
        print("\n","="*30,"\nStudent ID        :", sid)
        print("Gender            :",s['gender'])
        print("Total Marks       :", int(s['total_marks']), "/300")
        print("Percentage        :", round(pct, 2), "%")
        print("Rank | Percentile :", rank, "|", round(percentile, 2))
        print("\nSubject-wise Marks and Percentile : \n")
        rows = []
        for sub in marks_cols:
            sub_pct = ((df[sub] > s[sub]).sum() + 1) / len(df) * 100
            rows.append([sub, s[sub], "50", sub_pct])
        subject_df = pd.DataFrame(rows,columns=["Subject", "Marks", "Max Marks", "Percentile"])
        print(subject_df)
    except Exception as e:
        print("Error:", e)

#Heatmap correlation between different columns
def heatmap_seaborn():
    plt.figure(figsize=(10,8))
    sns.heatmap(df[marks_cols + lifestyle_cols + ['percentage']].corr(),annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

#Sleep vs overall percentage - scatter plot
def sleep_vs_performance(df):
    sns.scatterplot(x='sleep_hours', y='percentage', data=df)
    plt.title("Sleep Hours vs Performance")
    plt.show()

#Screen time vs overall percentage - scatter plot
def screen_vs_performance(df):
    sns.scatterplot(x='screen_time', y='percentage', data=df)
    plt.title("Screen Time vs Performance")
    plt.show()

#Average overall percentage section wise - box plot
def plot_section_performance(df):
    plt.figure(figsize=(10,6))
    sns.boxplot(x='section', y='percentage', data=df)
    plt.title("Section-wise Performance Comparison (Percentage)")
    plt.xlabel("Section")
    plt.ylabel("Percentage")
    plt.show()

def gender_performance(df):
    sns.boxplot(x='gender', y='percentage', data=df)
    plt.title("Gender-wise Performance Comparison")
    plt.show()

#Average overall percentage section wise - line chart
def section_avg_line(df):
    section_avg = df.groupby('section')['percentage'].mean().sort_index()
    plt.figure(figsize=(8,5))
    plt.plot(section_avg.index, section_avg.values, marker='o')
    plt.xlabel("Section")
    plt.ylabel("Average Percentage")
    plt.title("Section-wise Performance Trend")
    plt.ylim(20, 100)
    plt.grid(alpha=0.5)
    plt.show()

#Average marks subject wise- bar plot
def subject_difficulty_analysis(df):
    avg_marks = df[marks_cols].mean()
    avg_marks.plot(kind='bar')
    plt.title("Average Marks per Subject")
    plt.ylabel("Marks")
    plt.show()

#Variation subject wise -bar plot
def subject_variability(df):
    variability = df[marks_cols].std()
    variability.plot(kind='bar')
    plt.title("Subject-wise Variability")
    plt.ylabel("Std Deviation")
    plt.show()

#Subject wise - section wise averages - bar plot
def section_subject_average(df):
    section_avg = df.groupby('section')[marks_cols].mean()
    section_avg.plot(kind='bar', figsize=(10,6))
    plt.title("Section-wise Subject Average")
    plt.ylabel("Marks")
    plt.show()

#histogram with bins
def performance_distribution(df):
    bins = [0, 40, 60, 75, 90, 100]
    counts, _, _ = plt.hist(df['percentage'], bins=bins,edgecolor='black', rwidth=0.85)
    plt.xlabel("Percentage Range")
    plt.ylabel("Number of Students")
    plt.title("Student Performance Distribution")
    plt.xticks(bins)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    for i, count in enumerate(counts):
        plt.text((bins[i]+bins[i+1])/2, count+1, int(count),ha='center', fontsize=9)
    plt.show()

#Preview
class DataPreview:
    def __init__(self, df):
        self.df = df

    def head(self, n=5):
        print("\n--- HEAD ---")
        print(self.df.head(n))

    def tail(self, n=5):
        print("\n--- TAIL ---")
        print(self.df.tail(n))

    def info(self):
        print("\n--- INFO ---")
        self.df.info()

    def describe(self, cols=None):
        print("\n--- DESCRIBE ---")
        if cols is None:
            print(self.df.describe())
        else:
            print(self.df[cols].describe())

preview=DataPreview(df)

