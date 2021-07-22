import string

b=string.ascii_letters

print((b))
word="heyllob"



a=[3,5,7]

for i in enumerate(a):
    (a1,a2)=i
    print("item %s has index %s" %(a2,a1))

#############################

sm=[1,1,1,0,0,1,0,1,0]

res=[0]*sm.count(0)
ones=[1]*sm.count(1)

res.extend(ones)

print(res)
#########################

s="James Bond"

s=s[2::-1]

print(s)
##############

x=0
while x<100:
    x+=2
print(x)

###########

var=10
for i in range(10):
    for j in range(2,10,1):
        if var%2==0:
            continue
        var+=1
    var+=1
else:
    var+=1
print(var)
###########

x=0
for i in range(10):
    

