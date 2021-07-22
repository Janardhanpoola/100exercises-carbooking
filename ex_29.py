values=input("enter values : ")
lst=[]
for i in values.split(","):
    lst.append(i)
with open("planets.txt","a+") as f:
    f.seek(0)
    f.write("\n".join(lst))