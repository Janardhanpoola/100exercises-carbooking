import string
s="abcuhuvmnbaj"

s=s.lower()


chars=string.ascii_lowercase

vowels="aeiou"

cons=''.join(i for i in chars if i not in vowels)

filter=''.join(i for i in s if i not in cons)

if filter==filter[::-1]:
    print("palindrome")
else:

    print("not")

#############

l=string.ascii_lowercase
l=sorted(list(set(l)))
s="The quick brown fox jumps over the lazy dog"
s=s.lower()
s=''.join(s.split())


s=''.join(sorted(s))

s=sorted(set(s))


if l==s:
    print("pan")
else:
    print("no")


######################
#Python program to check if given value occurs atleast k times
#
test_list = [1, 3, 5, 5, 4, 5,5]  

val=5

k=3

sum=0

for i in test_list:
    if i==val:
        sum+=1
print(sum)

if sum>=k:
    print("yes")
else:
    print("no")

#############

#ipv4 ipv6 address check

def isipv4(s):
    try:
        return str(int(s))==s and 0<=int(s)<=255
    except:
        return "incorrect ipv4"


IP4="1233.6.5.4"

ipv4=IP4.split(".")

if len(ipv4)==4 and all(isipv4(n) for n in ipv4):
    print("valid ipv4")
else:
    print("no")


#ipv6

def isipv6(s):
    if len(s)>4:
        return False

    try:
        int(s,16) #it should be hexadecimal
        return True
    except:
        return False


v6="2001:0db8:85a3:0000:0000:8a2e:0370:733487"

ipv6=v6.split(":")

if len(ipv6)==8 and all(isipv6(n) for n in ipv6):
    print("valid ipv6")
else:
    print("not valid")

#Python Program to check whether it is possible to make a divisible by 3 number using all digits in an array


def remby3(arr,n):

    reminder=0
    for i in range(0,n):
        reminder=(reminder+arr[i])%3

    return reminder==0


arr=[30,40,50]
n=3
print(remby3(arr,3))


#Check if given array can be made 0 with given operations performed any number of times

arr=[1,1,3]

res=[0]*len(arr)


for i in range(0,len(arr)):
    
    arr[i]=arr[i]+2 
    mini=min(arr)
    arr=[i-mini for i in arr]
    print(arr)

    if arr==res:
        print("we can make array of 0")
        break
else:
    print(f"not possible..resultant array is {arr}")
#############

x = {'a': 1, 'b': 24}
y = {'b': 20, 'c': 11}
    
z={**y,**x}

print(z)
        
################
#Python | Merging two list of dictionaries

Input1 = [{'roll_no': ['123445', '1212'], 'school_id': 1}, 
          {'roll_no': ['HA-4848231'], 'school_id': 2}] 
Input2 = [{'roll_no': ['473427'], 'school_id': 2}, 
          {'roll_no': ['092112'], 'school_id': 5}] 
  
# Iterating and using extend to convert 
for elm1 in Input1: 
  
    for elm2 in Input2: 
        if elm2['school_id'] == elm1['school_id']: 
            elm1['roll_no'].extend(elm2['roll_no']) 
            break
    else:
        Input1.append(elm2) 
  
# printing  
print(Input1) 

##########################

test_list = [{'Gfg' : 3, 4 : 9}, {'is': 8, 'Good' : 2}]

l=[]
for i in enumerate(test_list):
    l.append(i)

print(dict(l))




