import sqlite3
import pandas as pd


filtered_coun=[]
con=sqlite3.connect("database/database.db")

cur=con.cursor()

cur.execute("select * from countries where area>2000000")

rows=cur.fetchall()

print(rows)


df=pd.DataFrame(rows)
df.columns=["A","B","C","D"]
#df1=df.drop([0],axis=0)
print(df)
df.to_csv("filtered.csv")