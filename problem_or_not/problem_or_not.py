import sys
sys.path.append('../')

import pandas as pd
import GoogleGemini as gg

df = pd.read_csv('/Users/risaonishi/Downloads/CS/UR2PhD/csv/ucr_submissions.csv')
df = df[['title','selftext']]
print(df)

gg.AskGoogleGemini()