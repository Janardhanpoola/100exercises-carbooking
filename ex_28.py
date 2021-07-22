with open("urls.txt") as f:
    con=f.readlines()
    con=[i.strip("\n") for i in con]
    con=[i.replace("https:/","http://") for i in con]
    #con=[i. for i in con]
    print(con)

strr="    hey   "
str=strr.strip()
print(str)