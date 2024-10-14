import sys
sys.path.append('../')

import pandas as pd
import GoogleGemini as gg
gg.InitGoogleGemini()

df = pd.read_csv('/Users/risaonishi/Downloads/CS/UR2PhD/csv/ucr_submissions.csv')
df = df[['title','selftext']]
df = df.sample(n=10, random_state=50)
problems = []

for index, row in df.iterrows():
    title = row['title']
    body = row['selftext']
    prompt = "Given this title:\n" + title + "\n And this body:\n" + str(body) + "\n Is this post a problem? Answer in only Yes/No"
    print(prompt)
    response = gg.AskGoogleGemini(prompt,force=True)
    problems.append(response)
    print('====='*20)


df['Problem'] = problems
df.to_csv('problem_submissions.csv', index=False)
print(df)