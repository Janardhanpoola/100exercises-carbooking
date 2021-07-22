# 0 1 1 2 3 5
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(0,3):
    print(fib(i))

##################


def fib1(n):
    a=0
    b=1
    for i in range(n):
        c=a+b   
        a=b
        b=c
    print(b)

fib1(4)

##########m
my_set={6,7,8}
print(type(my_set))

