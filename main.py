import pandas as pd

from word2number import w2n

# Main: Load data
df = pd.read_csv('grades.csv')

# Main: Preview data
print(df.head())

# Main: Inspect structure
print(df.info())
print(df.isna().sum())

# Main: Clean data

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

# Main: Final data preview
print(df.info())
print(df.isna().sum())

print(df.to_string())
