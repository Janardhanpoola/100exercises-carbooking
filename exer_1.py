import pandas as pd

df=pd.read_csv("smpl.csv")

df=df[df['SUITE NAME'].str.contains('PHY|SW')]

df=df[~df['SUITE NAME'].str.contains('VMX|EVO|RCB|rcb|COS|cos')]


new_df=df['JOB ID']#+df['TEST SUBMISSION ID']

print(new_df)





