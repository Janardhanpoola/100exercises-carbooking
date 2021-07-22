while(True):
    with open("users.txt","r") as f:
        content=f.readlines()
        content=[i[:-1] for i in content]
        
        print(content)
    un=input("enter un: ")
    if un in content:
        print("un already taken")
        continue

                

    pwd=input("Enter a new pwd ")
    if(any(i.isdigit() for i in pwd) and any(i.isupper() for i in pwd) and len(pwd)>=5):
        print("pwd is ",pwd)
        break
    if not (any(i.isdigit() for i in pwd)):
        print("enter atleast 1 digit" )
    if not (any(i.isupper() for i in pwd)):
        print("atleast one upper case")
    elif(len(pwd)<=5):
        print("should be >5")


    print("enter again")