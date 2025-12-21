# *Student Academic Performance & Lifestyle Impact Analyzer*

##Overview

This project analyzes student academic performance and studies the effect of lifestyle factors such as sleep hours and screen time using Python. The analysis is performed through a menu-driven, terminal-based program.

## *Objectives*

Clean and preprocess student academic data
Compute performance metrics such as percentage
Analyze overall and group-wise performance
Study the impact of sleep and screen time on academic results
Visualize insights using charts

## *Dataset*

Size: 368 students
Format: CSV
Columns:
Student ID, gender, 6 subject marks, sleep_hours, screen_time

*Data Source:*
The dataset is a derived dataset created using real-life academic records and patterns observed from publicly available Kaggle and GitHub datasets, with lifestyle values synthesized for educational analysis..

## *Tools Used*

Python
pandas, numpy
matplotlib, seaborn

## *Data Processing*

Invalid entries converted to NaN
Records with all marks missing removed
Absences treated as zero marks
Lifestyle values imputed using median
Duplicate records removed
Percentage calculated assuming each subject is out of 50

## *Analysis & Visualization*

Subject-wise and gender-wise performance analysis

Lifestyle factors vs academic performance

Bar charts, scatter plots, and box plots