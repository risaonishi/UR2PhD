import sys
sys.path.append('../')

#exec(open("../GoogleGemini.py").read())

import GoogleGemini as gemini
import pandas as pd
import statistics

gemini.InitGoogleGemini()

df = pd.read_csv('../problem_or_not/problem_submissions.csv')

def numeric(min, max):
    severity = []
    consistency = []

    df2 = pd.read_csv('severity.csv')

    for index, row in df.iterrows():
        if index >= min and index <= max and row['Problem'] == "Yes":
            title = row['title']
            text = row['selftext']
            prompt = "This reddit post describes a problem that someone is experiencing."
            prompt += " Given its title:\n" + title + "\n And the text of the post: \n" + str(text)
            prompt += "\n Rate the apparent severity of the problem, on a scale from 1 (least severe) to 10 (most severe). Give only a number."

            responses = []
            for x in range(3):
                responses.append(int(gemini.AskGoogleGemini(prompt, force=True)))

            severity.append(statistics.median(responses))
            consistency.append(round(statistics.stdev(responses), 2))
        else:
            severity.append(df2.iloc[index]['Severity'])
            consistency.append(df2.iloc[index]['Consistency'])

    df2['Severity'] = severity
    df2['Consistency'] = consistency
    df2.to_csv('severity.csv', index=False)

def numeric_justify(min, max):
    severity = []
    consistency = []

    df2 = pd.read_csv('severity_justify.csv')

    for index, row in df.iterrows():
        if index >= min and index <= max and row['Problem'] == "Yes":
            title = row['title']
            text = row['selftext']
            prompt = "This reddit post describes a problem that someone is experiencing."
            prompt += " Given its title:\n" + title + "\n And the text of the post: \n" + str(text)
            prompt += "\n Rate the apparent severity of the problem, on a scale from 1 (least severe) to 10 (most severe). Give only a number."
            prompt += " On the first line, answer only in terms of the number and only the number. On the second line, provide a justification."

            responses = []
            for x in range(3):
                response = gemini.AskGoogleGemini(prompt, force=True).split('\n')
                responses.append(int(response[0]))

            severity.append(statistics.median(responses))
            consistency.append(round(statistics.stdev(responses), 2))
        else:
            severity.append(df2.iloc[index]['Severity'])
            consistency.append(df2.iloc[index]['Consistency'])

    df['Severity'] = severity
    df['Consistency'] = consistency
    df.to_csv('severity_justify.csv', index=False)

def textual(min, max):
    severity = []
    change = []

    df2 = pd.read_csv('severity2.csv')

    for index, row in df.iterrows():
        if index >= min and index <= max and row['Problem'] == "Yes":
            title = row['title']
            text = row['selftext']
            prompt = "This reddit post describes a problem that someone is experiencing."
            prompt += " Given its title:\n" + title + "\n And the text of the post: \n" + str(text)
            prompt += "\n Rate the apparent severity of the problem, using only the descriptors 'Very serious', 'Moderately serious', 'Somewhat serious', 'Not very serious', and 'Not serious'."

            responses = []
            for x in range(2):
                responses.append(gemini.AskGoogleGemini(prompt, force=True))

            severity.append(responses[0])
            if responses[0] != responses[1]:
                change.append("True")
            else:
                change.append("False")
        else:
            severity.append(df2.iloc[index]['Severity'])
            change.append(df2.iloc[index]['Change'])

    df['Severity'] = severity
    df['Change'] = change
    df.to_csv('severity2.csv', index=False)

def textual_justify(min, max):
    severity = []
    change = []

    df2 = pd.read_csv('severity2_justify.csv')

    for index, row in df.iterrows():
        if index >= min and index <= max and row['Problem'] == "Yes":
            title = row['title']
            text = row['selftext']
            prompt = "This reddit post describes a problem that someone is experiencing."
            prompt += " Given its title:\n" + title + "\n And the text of the post: \n" + str(text)
            prompt += "\n Rate the apparent severity of the problem, using only the descriptors 'Very serious', 'Moderately serious', 'Somewhat serious', 'Not very serious', and 'Not serious'."
            prompt += " On the first line, answer only in terms of these phrases, verbatim. On the second line, provide a justification."

            responses = []
            for x in range(2):
                response = gemini.AskGoogleGemini(prompt, force=True).split('\n')
                responses.append(response[0])

            severity.append(responses[0])
            if responses[0] != responses[1]:
                change.append("True")
            else:
                change.append("False")
        else:
            severity.append(df2.iloc[index]['Severity'])
            change.append(df2.iloc[index]['Change'])

    df['Severity'] = severity
    df['Change'] = change
    df.to_csv('severity2_justify.csv', index=False)

#numeric(5, 9)
#numeric_justify(9, 9)
#textual(0, 9)
textual_justify(0, 9)
    




 

