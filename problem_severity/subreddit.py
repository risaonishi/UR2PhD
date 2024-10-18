import sys
sys.path.append('../')

import GoogleGemini as gemini
import pandas as pd

#exec(open("../GoogleGemini.py").read())

gemini.InitGoogleGemini()

#df = pd.read_csv('/Users/mattc/Downloads/UC_Subreddit_Data/UCR/ucr_submissions.csv')
df = pd.read_csv('../problem_or_not/problem_submissions.csv')
#df = df[['title', 'selftext']]
#df = df.sample(n=10, random_state = 50)
severity = []

for index, row in df.iterrows():
    if row['Problem'] == "Yes":
        title = row['title']
        text = row['selftext']
        prompt = "This reddit post describes a problem that someone is experiencing."
        prompt += " Given its title:\n" + title + "\n And the text of the post: \n" + str(text)
        prompt += "\n Rate the apparent severity of the problem, on a scale from 1 (least severe) to 10 (most severe)."
        response = gemini.AskGoogleGemini(prompt, force=True)
        severity.append(response)
    else:
        severity.append(0)

df['Severity'] = severity
df.to_csv('severity.csv', index=False)


    




 

