with open("countries_missing.txt") as f1:
    con=f1.readlines()
    con=[i.strip("\n") for i in con]
    #print(con)
missing_coun=["porutgal","Germany","spain"]
con1=[con.append(i) for i in missing_coun if i not in con]

#for i in missing_coun:
#    if i not in con:
#        con.append(i)




print(con1)