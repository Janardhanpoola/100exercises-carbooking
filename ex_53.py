def aps(arr,t):
    lnth=len(arr)
    for i in range(0,lnth):
        for j in range(i+1,lnth):
            if arr[i]+arr[j]==t:
                print(str(arr[i])+","+str(arr[j]))

(aps([4,5,3,6,1,8,7,3],9))
################

from collections import Counter
def ew(a):
    d={}
    for i in a:
        d[i]=d.get(i,0)+1
    return d

a=[1,2,3,4,5,4,3,2,1]

b=[1,2,3,4]

a.extend(b)

res=ew(a)
print(res)

for i in res:
    if res[i]==1:
        print(i)



#########Largest continous sum########

def large_sum(lst):
    max_sum=current_sum=0
    for num in lst[1:]:
        current_sum=max(current_sum+num,num)
        max_sum=max(current_sum,max_sum)
    return max_sum


print(large_sum([1,2,3,4,0,8]))


#################

sen="  This    is  best  "

sen=sen.split()


lst=[]
for i in range(len(sen)-1,-1,-1):   
    lst.append(sen[i])

res=" ".join(lst)
print(res)

##############

import re
s="ABC12DEF3G56HIJ7ABC12"
res=[]
unq=set(s)

pattern=re.compile(r'([A-Z]+)([0-9]+)')

matches=pattern.finditer(s)

for i in matches:
    print(i.group(1),'*',i.group(2))

######################


d={}

s="ABC"
flag=0
for i in s:
    d[i]=d.get(i,0)+1

print(d)

res=[i for i in d.values() if i>1]

if res!=None:
    print("nu")
else:
    print("UNQ")


###################

s1="abbbggf"

#s1="aabbccd"
flag=0
s1=Counter(s1)
print(s1)
sl=[]
flag=0
for i in s1.values():
    sl.append(i)

print(sl)

for i in sl:
    if i>1:
        flag=1
if flag==1:
    print("no")
else:

    print("yes")
    
##################

#another approach

s="abcd"

b=1
e=len(s)
f=0
while b<e:
    if s[b]==s[b-1]:
        f=1
        break
    else:
        b+=1
if f==1:        
    print("NU")
else:
    print("U")


