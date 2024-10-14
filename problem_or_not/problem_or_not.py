import pandas as pd
df = pd.read_csv('csv/ucr_submissions.csv')
df = df[['title','selftext']]
print(df)
