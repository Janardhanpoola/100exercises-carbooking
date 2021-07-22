with open("sm.txt","r") as f:
    content=f.readlines()
    print(content)

    #res=sum([len(i[:-1]) for i in content])
    res=[i[:-1] for i in content]
    print(res)

    str_res=" ".join(res)
    print(str_res)
    print(len(str_res))

    res=str_res.replace(" ","")

    print(len(res))