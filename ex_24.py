import sqlite3

con=sqlite3.connect("database/database.db")

cursor=con.cursor()

cursor.execute("SELECT country FROM countries where area>2000000")
rows=cursor.fetchall()
print(rows)
con.close()

for i in rows:
    print(i[0])