while(True):
    with open("users.txt") as f:
        content=f.readlines()
        #print(content)
        users=[i.strip("\n") for i in content]
        #print(users)
    
    un=input("enter un ")
    for i in users:
        if un in i:
            print("already exists")
            continue
    
    break

while(True):
    pwd=input("enter pwd")
    if not (any(e.isdigit() for e in pwd )):
        print("atleast 1 digit")
    if not (any(i.isupper() for i in pwd)):
        print("atleast one upper char")
    if(len(pwd)<5):
        print("should be >5")
    else:
        print("pwd is fine")
        break




    
        