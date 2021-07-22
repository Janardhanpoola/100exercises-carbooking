l=[1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]


ls=set(l)
print(ls)

low=[]
high=[]


for i in ls:
    count=l.count(i)
    low.append(l.index(i))
    high.append(l.index(i)+count-1)

l=set(low)
h=set(high)

lh=list(zip(l,h))

lss=list(ls)

res=list(zip(lss,lh))

print("set is {}".format(res))