#print Nth node from the end of LL

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class SLL:
    def __init__(self):
        self.head=None

    def add_ele(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    
    def Nth_from_end(self,N):
        temp=self.head
        l=0
        while temp:
            temp=temp.next
            l+=1
        pos=l-N
        #print(pos)
        temp=self.head
        for i in range(0,pos):
            temp=temp.next
        print("data is ",temp.data)



ll1=SLL()

#ll1.head=Node(1)
#s=Node(2)
#t=Node(3)

#ll1.head.next=s
#s.next=t

ll1.add_ele(6)

ll1.add_ele(3)
ll1.add_ele(7)
ll1.add_ele(5)

ll1.Nth_from_end(2)

ll1.display()

##################
import time
def abc(x):
    try:
        #raise KeyboardInterrupt
        print(x)
        #raise KeyboardInterrupt
        time.sleep(1000)
    except KeyboardInterrupt:
        print("caught")

abc("hey")