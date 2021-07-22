import string
with open("countries_raw.txt","r") as f:
    content=f.readlines()
    print(content)
    content=[i.strip("\n") for i in content]
    print(content)
    content=[i for i in content if len(i)!=1]
    print(content)
    content=[i for i in content if i!=""]
    print(content)
    content=[i for i in content if i!="Top of Page"]
    print(content)



with open("new_coun.txt","w") as f1:
    for i in content:
        f1.write(i+"\n")


