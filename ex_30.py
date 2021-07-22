lst=[]
while True:
    ip=input("write something:  ")
    lst.append(ip)
    if(ip.lower()=="close"):
        break
print(lst)

with open("ipfile1.txt","a+") as f1:
    for i in lst[:-1]:
        f1.write(i+"\n")