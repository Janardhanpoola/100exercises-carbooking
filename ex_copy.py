sl=[1,2,3]
s2=sl
print(s2,sl) #same mem loc.

################


import copy

l1=[1,2,3]

l2=copy.copy(l1)

l2[0]=100
print(l2,l1)# diff values in both lists

########
#shallow copy
#########3
li1=[[1,2,3,4],[78,90],8]

li2=copy.copy(li1)

li2[1][1]=100
li2[2]=57

print(li2)
print(li1)#lists will have same vals.#in nested list ..if a value changed inside a list in li2 then that would be reflected in li1 as well

# li2.append([6,7])

# print(li2)
# print(li1)#lists will have diff values

##############
#deep copy (normal list)
###############

li1=[1,3,45]

li2=copy.deepcopy(li1)

li2[0]=788

print(li2,li1) #same as shallow copy..diff values in both lists

#nested list

l1=[[1,2,3],[9,0,6]]

l2=copy.deepcopy(l1)

l2[0][0]=987

print(l2,l1) #both have diff vals. #l2 will have 987 in index 0 of 1st nested list and l1 will be same as initial one







