test_list = ["GfG", "", "", "", "", "is", "", "", "best","best","33sumdon","33"]

d={}
i1=[]
for i in test_list:
    if i.isalpha() or i.isdigit() or i.isalnum():
      i1.append(i)

for e in i1:
    d[e]=d.get(e,0)+1

print(d)





print('ahy ?jj'.title())




d1={1:2,3:5}
d2={1:10}
for i in d1:
    print(i)

print(10+2)




e=[[[1,2],[3,4]]]
print(e[0])    

i=1

while True:
    if i%3==0:
        break 
    print(i)
    i+=1


d1={"cherry":"aunty","bhavi":"peddamma"}

d2={"bhavi":"dumbo","cherry":"jumbo"}

############################
#Merge dicts
#####################

from itertools import chain
from collections import defaultdict
dict1 = {"cherry":"aunty","bhavi":"peddamma"}
dict2 = {"bhavi":"dumbo","cherry":"jumbo"}
dict3 = defaultdict(list)

for k,v in chain(dict1.items(), dict2.items()):
    print(k,v)
    dict3[k].append(v)
 
print((dict(dict3)))


###################333

dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 

dic1.update(dic2)
print(dic1)




d={211:22,34:2,10:3}

a=[d[k] for k in sorted(d.keys())]

print(a)




v1=True
v2=False
v3=False

if v1 or v2 and v3:
    print("Y")

else:
    print("N")