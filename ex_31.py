f1= open("new22.txt","a+") 
while(True):
    ip=input("write somthing")
    if(ip=="CLOSE"):
        f1.close()
        break
    elif(ip=="SAVE"):
        #f1.close()
        f1=open("new22.txt","a+")
        
    else:
        f1.write(ip+"\n")