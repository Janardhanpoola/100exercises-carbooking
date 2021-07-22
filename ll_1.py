#Appending at the front SLL

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class SLL:
    def __init__(self):
        self.head=None

    def insert_at_front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next

    def insert_at_random(self,prev_node,data):
        if prev_node.next is None:
            return "not possible"
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node     

    def insert_at_last(self,data):   
        new_node=Node(data)
        last=self.head
        while last.next is not None:
            last=last.next
        last.next=new_node

    def del_node(self,key):
        cur_node=self.head
        #case 1: if current node to be deleted is the head
        if cur_node is not None and cur_node.value==key:
            self.head=cur_node.next
            cur_node=None
            

        #case 2: if cur_node to be deleted is not the head 
        prev=None
        while cur_node is not None and cur_node.value!=key:
            prev=cur_node
            cur_node=cur_node.next
        if cur_node is None:
            print("key is not found in LL")
        else:
            prev.next=cur_node.next
            cur_node=None 
        



ll1=SLL()

ll1.head=Node(1)
s=Node(2)
t=Node(3)

ll1.head.next=s

s.next=t

ll1.insert_at_front(55)

ll1.insert_at_random(s,56)

ll1.insert_at_last(57)

ll1.del_node(55)

ll1.display()