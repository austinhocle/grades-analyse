import pandas as pd

# Load data
df = pd.read_csv('grades.csv')

# Preview data
print(df.head())

# Inspect structure
print(df.info())
print(df.isna().sum())