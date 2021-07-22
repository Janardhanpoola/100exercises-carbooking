class stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def disp(self):
        #sort_items= [i for i in self.items()]
        print(sorted(self.items,reverse=True))


s1=stack()
s1.push(21)
s1.push(433)
s1.push(167)
s1.push(91)
s1.disp()


############

def trip(arr):
    arr.sort()
    for i in range(len(arr)-2):
        if arr[i]+arr[i+1]>arr[i+2]:
            print(arr[i],arr[i+1],arr[i+2])




trip([1,2,3,4,5,7,32,30])

##############

for i in range(1,6):
    print(i*'*')
    