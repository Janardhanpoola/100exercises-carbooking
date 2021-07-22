from collections import Counter
import string
def str_op(str1):

    lnth=len(str1) 
    if(lnth>=7):
        half=lnth//2
        res=str1[half-1]+str1[half:half+2]
        print(res)
    else:
        print("string should be >7")
str_op("JhonDIPPeta")
str_op("JasonAy")
str_op("hey")

def mid(s1,s2):
    lnth=len(s1)
    s1_mid=lnth//2
    res=s1[0:s1_mid]+s2+s1[s1_mid:]
    print(res)
s1 = "Ault"
s2 = "Kelly"
mid(s1,s2)

def st_op(s1,s2):
    lnth=len(s1)
    s1_mid=lnth//2
    s2_mid=len(s2)//2
    #s1_f=s1[1]+s1[s1_mid]+s1[-1]
    #s2_f=s2[1]+s2[s2_mid]+s2[-1]
    s3=s1[0]+s2[0]+s1[s1_mid]+s2[s2_mid]+s1[-1]+s2[-1]
    
    print(s3)

s1 = "America"
s2 = "Japan"
st_op(s1,s2)


def lower_first(s1):
    op=""
    up=""
    for i in s1:
        if i.islower():
            op=op+i
        elif i.isupper():
            up=i+up


    print(op+up)
        
    
s1 ="PyNaTive"
lower_first(s1)


def ca(s):
    d=0
    char=0
    spcl=0
    for i in s:
        if i.isdigit():
            char+=1
        elif i.isalpha():
            d+=1
        else:
            spcl+=1
    print(d,char,spcl)

ca("P@#yn26at^&i5ve")



def usa(s,t):
    s=s.lower()
    count=s.count(t)
    print(count)



usa("Welcome to USA. usa awesome, isn't it?","usa")


def avg(s):
    s=s.split()
    s1=[]
    print(s)
    for i in s:
        if i.isdigit():
            s1.append(int(i))
    total=sum(s1)
    avg=total/len(s1)
    print(total,avg)

avg("English = 78 Science = 83 Math = 68 History = 65")    


def oc(s):
    total=Counter(s)
    print(total.items())

oc("Apple")



def fin(s,t):
    i=s.rfind(t)
    print(i)
        

fin("Emma is a data scientist who knows Python. Emma works at google.","Emma")

def e(l):
    for i in l:
        if ""  in l:
            l.remove("")
        elif None in l:
            l.remove(None)
    print(l)


e(["Emma", "Jon", "", "Kelly", None, "Eric", ""])

def spc(s):
    pun="/*@&"
    for i in s:
        if i in pun:
            s=s.replace(i,"")
    print(s)

spc("/*Jon is @developer & musician")


def aln(s):
    res=[]
    temp=s.split()
    print(temp)
    for item in temp:
        if any(i.isalpha() for i in item) and any(i.isdigit() for i in item):
            res.append(item)
    print(res)

aln("Emma25 is Data scientist50 and AI Exper")


a=['Emma25', 'is', 'Data', 'scientist50', 'and', 'AI', 'Exper']
b=[]
for i in a:
    if i.isalnum() and not i.isalpha() and not i.isdigit():
        b.append(i)
print(b)

sampleDict = dict([
('first', 1),
('second', 2),
('third', 3)
])