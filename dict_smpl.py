d={'ename':['visaal','janardhan','xyz'],'empid':[1,2,3]}

res=list(d.values())

for i in zip(res[0],res[1]):
    print(i)



    


# res=[i for i in zip(list(values))]

# print(res)

# for a,b in zip(list(items)):
#     print(a)
# mapped=zip(values)

# print(set(mapped))

# #visaal,janardhan,xyz



# class Employee:

#     def __init__(self,emp_name,emp_id):
#         self.emp_name=emp_name
#         self.emp_id=emp_id

# Emp1=Employee("jana","1")

# print(Emp1.emp_id)
# print(Emp1.emp_name)

# Emp1.emp_id=2

# print(Emp1._emp_name)

res=lambda x:x**2

print(res(4))

############

test_dict = {'gfg' : [5, 6, 7, 8], 
             'is' : [10, 11, 7, 5], 
             'best' : [6, 12, 10, 8], 
             'for' : [1, 2, 5]} 
             

res=list(test_dict.values())

for i in zip(res[0],res[1]):
    print(i)


#####################


test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21} 


#del test_dict["Mani"]

# removed_val=test_dict.pop("Mani")

# print(removed_val)
# edict={}
# for k,v in test_dict.items():
#     if k!="Mani":
#         edict[k]=v

# print(edict)        
        
    
res={k:v for k,v in test_dict.items() if k!="Mani" }

print(test_dict)


dict1 = {'a': 10, 'b': 8}
dict2 = {'b': 6, 'c': 4}

res={**dict1,**dict2}

print(res)

#########

#Print anagrams together in Python using List and Dictionary

arr = ['cat', 'dog', 'tac', 'god', 'act']

d={}

for i in arr:
    key="".join(sorted(i))
    
    
    if key in d.keys():
        d[key].append(i)
    else:
        d[key]=[]
        d[key].append(i)
        
print(d)


        
####################


import string
ip="pneumonia"

alphas=string.ascii_lowercase
rev_alphas=string.ascii_lowercase[::-1]
print(alphas)
print(rev_alphas)

res=dict(zip(alphas,rev_alphas))
print(res)

N=4
s=ip[0:N-1]
for i in range(N-1,len(ip)):
    s=s+res[ip[i]]

print(s)
#####################
#Possible Words using given characters in Python

from collections import Counter

Dict = ["go","bat","me","eat","goal","boy", "run"]

arr = ['e','o','b', 'a','m','g', 'l']

for e in Dict:
    chars=Counter(e)
    #print(chars)
    flag=1
    for key in chars.keys():
        if key not in arr:
            flag=0
        else:
            if arr.count(key)!=chars[key]:
                flag=0
    if flag==1:
        print(e)
        

##########
#Python – Keys associated with Values in Dictionary
test_dict = {'abc' : [10, 30], 'bcd' : [30, 40, 10]}

#{10: [‘abc’, ‘bcd’], 30: [‘abc’, ‘bcd’], 40: [‘bcd’]}


vals=list((test_dict.values()))

s=[]
for i in vals:
    for j in i:
        s.append(j)
        


s=list(set(s))
print(s)

t={}
for i in s:
    l=[]
    for k,v in test_dict.items():
        if i in v:
            l.append(k)
            t[i]=l
            
print(t)    

############

test_list = [{"gfg" : 1, "is" : 4, "best" : 9},

             {"gfg" : 6, "is" : 3, "best" : 8},

             {"gfg" : 1, "is": 4, "best" : 9},

             {"gfg" : 1, "is" : 1, "best" : 9},
             
             {"gfg" : 6, "is" : 3, "best" : 8}]


vals=[]
for i in test_list:
    vals.append(list(i.values()))

counts=[]
for i in vals:
    counts.append(vals.count(i))
print(counts)

test_list=[str(i) for i in test_list]

res=list(set(list(zip(test_list,counts))))

print(res)

################
#Python Program to calculate Dictionaries frequencies

from collections import Counter 
  
# initializing list 
test_list = [{'gfg': 1, 'is': 4, 'best': 9}, 
             {'gfg': 6, 'is': 3, 'best': 8}, 
             {'gfg': 1, 'is': 4, 'best': 9}, 
             {'gfg': 1, 'is': 1, 'best': 9}, 
             {'gfg': 6, 'is': 3, 'best': 8}] 
  
# for i in test_list:
#     for k in i.items():
#         print(k)

#c=[ tuple(sorted(k.items())) for k in test_list]
c=[ tuple((k.items())) for k in test_list]

print(c)

cnt=Counter(c)

print(cnt)
keys=list(cnt.keys())

# res=[]
# for key in keys:
#     res.append(dict(key))

keys=[dict(key) for key in keys]

vals=list(cnt.values())

res=list(zip(keys,vals))

print(res)
    




#fkeys={dict(k):v for k,v in cnt.keys()}


#print(d_keys)

###############
#Python – Extract digits from Tuple list


test_list = [(15, 3), (3, 9)]

l=[]
l2=[]
for i in test_list:
    a,b=i
    l.append(a)
    l2.append(b)

l.extend(l2)

print(l)

l=[str(i) for i in l]

print(l)

res=[]
for i in l:
    if len(i)>1:
        for j in i:
            res.append(j)
    else:
        res.append(i)
        
res=[int(i) for i in res]
print(res)
################
# All pair combinations of 2 tuples
# 
test_tuple1 = (9, 2)
test_tuple2 = (7, 8)



f=[(a,b) for a in test_tuple1 for b in test_tuple2]+[(a,b) for a in test_tuple2 for b in test_tuple1]
        
print(f)    

    
################
#Remove Tuples of Length K

test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7),(5,6)]

k=4

res=[i for i in enumerate(test_list) if len(i[1])==k]

print(res)

for i in res:
    test_list.remove(i[1])

print(test_list)


########

# program to sort a list of tuples by second Item

l=[('for', 24), ('Geeks', 8), ('Geeks', 30)] 

#[('Geeks', 8), ('for', 24), ('Geeks', 30)]

#l=[i for i in l]

l=sorted(l,key=lambda x:x[1])

print(l)
##############

#Order Tuples by List

test_list = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]

ord_list = ['Geeks', 'best', 'CS', 'Gfg']

l=[]
for i in ord_list:
    for j in test_list:
        if i==j[0]:
            l.append(j)

print(l)
##ORRR###
test_list = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]

ord_list = ['Geeks', 'best', 'CS', 'Gfg']

d=dict(test_list)

res=[(i,d[i]) for i in ord_list]

print(res)
    
######
#Flatten tuple of List to tuple

test_tuple = ([1],[1,2],[1,2,4])

l=[]
for i in test_tuple:
    if type(i)!=list:# if ip is ([5,5,7])
        l.append(i)
    else:
        for j in i:# if ip=([1],[1,2],[1,2,4])
            l.append(j)
print(tuple(l))

#############
# Convert Nested Tuple to Custom Key Dictionary

test_tuple = ((1, 'Gfg', 2), (3, 'best', 4))

#res=[{'key':i[0],'value':i[1],'id':i[2]} for i in test_tuple] # one liner answer

#keys = [‘key’, ‘value’, ‘id’]
# [{‘key’: 1, ‘value’: ‘Gfg’, ‘id’: 2}, {‘key’: 3, ‘value’: ‘best’, ‘id’: 4}]

d={}

keys=['key','value','id']

vals=[list(i) for i in test_tuple]

print(vals)

l=[]
for i in range(0,len(vals)):
    l.append(dict(zip(keys,vals[i])))

print(l)
    

#########

#Python Program to Remove duplicate tuples irrespective of order
test_list = [(4, 6), (1, 2), (9, 2), (2, 1), (5, 7), (6, 4), (2,9)]

for i in test_list:
    for j in test_list[1:]:
        if i[0]==j[1] and i[1]==j[0]:
            test_list.remove(j)

print(test_list)## takes 50 steps to execute
######

test_list = [(4, 6), (1, 2), (9, 2), (2, 1), (5, 7), (6, 4), (2,9)]

res=[tuple((sorted(list(i)))) for i in test_list] 

print(list(set(res))) #takes 13 steps to execute


################
#convert 1st to +ve ...2nd to negative

test_list = [(3, -1), (-4, -3), (1, 3), (-2, 5), (-4, 2), (-9, -3)]

res=[]

for i in test_list:
    if i[1]>0:
        res.append((abs(i[0]),-i[1]))
    else:
        res.append((abs(i[0]),i[1]))

print(res)

res=[ (abs(i[0]),-i[1]) if i[1]>0  else (abs(i[0]),i[1])  for i in test_list]

print(res)
##############
#print lists divisible by given num

est_list = [[5, 10, 15], [4, 8, 12], [100, 15], [5, 10, 23]]
#[[4, 8, 12]] 
k=4

#res=[ele for ele in est_list if all(i%k==0 for i in ele)]
res=[]
for ele in est_list:
    if all(i%k==0 for i in ele):
        res.append(ele)

print(res)
            

#####
# 
# Python3 code to demonstrate working of
# Join Tuples if similar initial element
# Using defaultdict() + loop
from collections import defaultdict

# initializing list
test_list = [(5, 6), (5, 7),(5,8), (6, 8), (6, 10), (7, 13)]

d=defaultdict(list)

for k,v in test_list:
    d[k].append(v)
print(d)        