dict1={'bhavi':{'age':8,'schl':'SC'}, 'cherry':{'age':5,'schl':'govt'}}

for i in dict1:
    print(i)
    for e in dict1[i]:
        print(e,":",dict1[i][e])


def fast(items= []):
    items.append (1)
    return items

print(fast())
print(fast())



L=[1,2,3]

print(L[-2])