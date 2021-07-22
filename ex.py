
def prime(num):


    prime1=[]
    for i in range(2,num):
        if num%i==0:
            #print("not a prime")
            break 
    else:
        prime1.append(num)
        print(prime1)
    
prime(50)
        #print(num)
#for i in range(2,50):
#    prime(i)

###############

def prime_factors(num):
    factors=[]
    divisor=2
    while(divisor<=num):
        if num%divisor==0:
            factors.append(divisor)
            num=num/divisor
        else:
            divisor+=1
    return factors

print(prime_factors(120))


##########3  madam  malayalam suus

def palin(s):
    s1=''
    s=s.lower()
    garbage=['-',"'"]
    print(s)
    l=len(s)+1
    for i in s[-1:-l:-1]:
        s1+=i
    print(s1)
    if s==s1:
        print("yes")
    else:
        print("no")

palin("gohan gasal amimalasa'-gnahog")

##########################
import string
def palin_sent(s):
    s=s.lower()
    chars=string.ascii_lowercase
    s=''.join(i for i in s if i in chars)
    if s==s[::-1]:
        return True
    return False
print(palin_sent("gohan gasal amimalasa'-gnahog"))

###########

# bana

def sort_sen(s):
    s=s.split()
    s.sort(key=str.casefold)
    print(s)


(sort_sen("JACK apple BANANA ORANGE"))
###########

#sorting mtd 2:

def sort_ss(s):
    s=s.split()
    print(s)
    s=[word.lower()+word for word in s]
    s=sorted(s)
    s=[word[(len(word)//2):] for word in s]
    print(s)

(sort_ss("JACK apple BANANA ORANGE"))

#############

def index_all(lst,num):
    indices=[]
    for i in range(len(lst)):
        if num==lst[i]:
            indices.append([i])
        elif isinstance(lst[i],list):
            for index in index_all(lst[i],num):
                #indices.append([i])
                indices.append([i]+index)
    return indices



lst=[ [[1,2,3],2,[1,3]],[1,2,3] ,2 ]

print(index_all(lst,2))


####3
import time,random
def waiting_game():

    target=random.randint(2,4)

    print(f'your target time is {target} seconds')

    input("--Press enter to begin--")

    start=time.perf_counter()
    print(start)

    input(f"press enter after {target} seconds")

    print(time.perf_counter())

    elapsed=time.perf_counter()-start

    print("elasped time is {} seconds".format(elapsed))

    if elapsed==target:
        print("perfect")
    elif target>elapsed:
        print("{0:.3f} secs too fast ".format(target-elapsed))
    else:
        print("{0:.3f} secs too slow ".format(elapsed-target))

#waiting_game()

#################

#def save_dic_to_file(d,path):
   
#    with open(path,"w") as f:

#        f.write(d)

#d="hey"
#save_dic_to_file(d,'sm1.txt')

colours = [["#660000","#863030","#ba4a4a","#de7e7e","#ffaaaa"],["#a34b00","#d46200","#ff7a04","#ff9b42","#fec28d"],["#dfd248","#fff224","#eefd5d","#f5ff92","#f9ffbf"],["#006600","#308630","#4aba4a","#7ede7e","#aaffaa"]]

target="#660000"

for i, c in enumerate(colours):
    #print(i,c)
    if target in c:
        print((i,c.index(target)))


#######

d={'1':'e','c':'i'}

print(d['1'])