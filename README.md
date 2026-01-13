# Grades Analyser

#### Context

An IT student wants to analyse their academic performance after completing their first year of university in order to identify which units they performed the best and worst in. This analysis helps determine areas of strength and highlights units that may require further improvement, and identifies units that could be pursued further in future years of study. 

This project is a Python-based analysis tool that uses sample data from the units completed by a first year IT student (Computer Science major) at QUT, to process and analyse data stored in CSV files. 

#### Purpose
The program loads the dataset into a Pandas Dataframe, cleans the data by handling empty cases, checking for duplicates and correcting inconsistent word formatting. 

It then performs a basic analysis, such as calculating average scores and identifying the strongest and weakest units, to evaluate which unit requires further improvement. 

#### Tasks
* What is the average grade percentage through all the subjects?
* What is the best performed subject? 
* What is the worst performed subject? 


#### Third-Party Python Packages used: 
* pandas 
* word2number

The dataset is included as [grades.csv](grades.csv) 