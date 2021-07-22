import pandas as pd   
import sqlite3

df=pd.read_csv("ten_more_countries.txt")

con=sqlite3.connect("database/database.db")

cur=con.cursor()
for r,c in df.iterrows():
    print(c["Country"],c["Area"])
    cur.execute("Insert into countries values (NULL,?,?,NULL)",(c["Country"],c["Area"]))  #id is null cause it automatically assigns a no.,pop is null since those vals aren't present

con.commit()
con.close()
