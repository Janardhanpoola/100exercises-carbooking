str1='geekforgeeks best for geeks'

str1=str1.split()

lookp_dict = {"best" : "good and better", "geeks" : "all CS aspirants"} 

res=[]

for i in str1:
    res.append(lookp_dict.get(i,i))

res=" ".join(res)

print(res)


ls=[1,2,3,4,5,6]

lk_dict={}
res=[]

for i in ls:

    res.append(lk_dict.get(i,i))
print(res)
#######################
import re

st1='geekforgeeks best for geeks'

pattern=re.sub(r'best','good and better',st1 and re.sub(r'geeks','thops',st1) )

print(pattern)

