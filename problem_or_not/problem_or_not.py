import sys
sys.path.append('../')

import pandas as pd
import GoogleGemini as gg
gg.InitGoogleGemini()

df = pd.read_csv('/Users/risaonishi/Downloads/CS/UR2PhD/csv/ucr_submissions.csv')
df = df[['title','selftext']]
df = df.sample(n=10, random_state=500)
problems = []

# for index, (i, row) in enumerate(df.iterrows(), start=1):
#     title = row['title']
#     body = row['selftext']
#     print(f"{i}. Title: {title}\n")
#     print(f"Body: {body}\n\n")

# df.to_csv('output.csv', index=False)
# quit()

for index, row in df.iterrows():
    title = row['title']
    body = row['selftext']
    prompt = f"""
        Given this title:\n{title}\n
        And this body:\n{str(body)}\n
        Is this post describing a 'problem' in the sense of an issue, challenge, or complaint people experience, like 'there's not enough parking on campus'? 

        A 'problem' should involve something people want to change or improve, typically related to daily life, services, or the environment around them.

        A post is *not a problem* if it:
        1. **Describes** general information, advice, or ideas without raising a specific issue.
        2. Is misleading, low-quality, or off-topic content, such as an empty post claiming to provide advice without actual details.
        
        **Examples:**
        - *Problem*: "Classes are so overcrowded this year; it's hard to find a seat."
        - *Problem*: "I wish the university would add more bike racks; there’s never anywhere to park my bike."
        - *Not a problem*: "I made a video on how to learn programming (but doesn’t include actual advice)."
        - *Not a problem*: "Check out this funny meme about college life!"

        If the body is empty or NaN, determine based on the title alone if it suggests a problem. If the title is empty, classify the post as *not a problem*.
        
        Answer with 'Yes' or 'No' and provide a brief justification as to why.
        """
    response = gg.AskGoogleGemini(prompt)
    problems.append(response)
    print('====='*20)


df['Problem'] = problems
df.to_csv('problem_submissions.csv', index=False)
print(df)