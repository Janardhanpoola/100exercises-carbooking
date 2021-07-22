def replc(str1,dict):
    s1=str1
    test_str=str1.split()
    t=list(dict.keys())
    t=t[0]
    #print(t)
    for i in test_str:
        if t==i:
            str1=str1.replace(i,dict[t])
            #print(str1)
        
    if(s1==str1):
         print("no string found to replace")
   
    return str1




str1 = "geekforgeeks best for geeks"

dict={"geeks":"all CS"}

#print(dict['geeks'])

print("string is",replc(str1,dict))

#####################
import re
s = "geekforgeeks best for geeks"

pattern=re.sub(r'\Bgeeks','CS',s)

print(pattern)