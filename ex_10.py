import requests
response = requests.get("http://www.pythonhow.com/data/universe.txt",headers = {'user-agent': 'customUserAgent'})
text = response.text
print(text.count('a'))

##########

tr="au123"

if tr.isalnum():
    print("y")


##########

def smpl(**kwrgs):
    for i,j in kwrgs.items():
        print(i,j)

smpl(a=1,b=2)

#########


def smp(*args):
    for a in args:
        print(a)

smp(1,2,3,4)

###########


def prime(num):
    for i in range(num):
        if i%2!=0 and num%i!=0:
            print(i)

prime(7)