class Deque():
    def __init__(self):
        self.items=[]
    def add_front(self,item):
        self.items.append(item)
    def add_rear(self,item):
        self.items.append(item)
    def remove_front(self):
        self.items.pop()
    def remove_rear(self):
        self.items.pop(0)

    def display(self):
        print(self.items)


d=Deque()

d.add_front(1)
d.add_front(2)
d.add_front(3)
d.add_rear(4)
d.add_rear(5)
d.add_rear(6)

d.remove_front()

#d.display()

d.remove_rear()

d.display()