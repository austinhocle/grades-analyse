import pandas as pd

from word2number import w2n

# 1. Load data
df = pd.read_csv('grades.csv')

# 2. Preview data
print(df.head())

# 3. Inspect structure
print(df.info())
print(df.isna().sum())

# 4. Clean data

# -> Convert string numbers to numeric values
def text_to_num(text):
    try:
        return w2n.word_to_num(text.replace('-', ' '))
    except:
        return text

df['Score'] = df['Score'].apply(text_to_num)
df['MaxScore'] = df['MaxScore'].apply(text_to_num)

df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
df['MaxScore'] = pd.to_numeric(df['MaxScore'], errors='coerce')

# -> Remove NaN entries in 'Score' and 'MaxScore' columns
df.dropna(subset=['Score', 'MaxScore'], inplace=True)

# -> Check for duplicates
print ("Duplicates found:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

# 5. Preview the final data after cleaning
print(df.info())
print(df.isna().sum())

print(df.to_string())


# 6. Calculate percentage
df['Percentage'] = (df['Score'] / df['MaxScore']) * 100


# 7. Calculate average grade percentage
average_percentage = df['Percentage'].mean()
print(f"The average grade percentage calculated for all subjects was {round(average_percentage, 2)}%.")

# 8. Calculate best subject
subject_totals = df.groupby("Subject").agg(total_score=('Score', 'sum'), total_max_score=('MaxScore', 'sum'))
subject_totals = subject_totals.copy()
subject_totals['TotalPercentage'] = (subject_totals['total_score'] / subject_totals['total_max_score']) * 100

best_row = subject_totals.loc[subject_totals['TotalPercentage'].idxmax()]

best_subject = best_row.name
best_subject_percentage = best_row['TotalPercentage']

print(f"The best performed subject was {best_subject} with a percentage of {round(best_subject_percentage, 2)}%.")

# 9. Calculate worst subject

worst_row = subject_totals.loc[subject_totals['TotalPercentage'].idxmin()]

worst_subject = worst_row.name
worst_subject_percentage = worst_row['TotalPercentage']

print(f"The worst performed subject was {worst_subject} with a percentage of {round(worst_subject_percentage, 2)}%.")