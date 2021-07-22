#BST IMPLEMENTATION

class Tree:
    def __init__(self,root):
        self.root=root
        self.leftC=None
        self.rightC=None
    

    def insert_Left(self,value):
        if self.leftC==None:
            self.leftC=Tree(value)
        else:
            t=Tree(value)
            t.leftC=self.leftC
            self.leftC=t
        #return self.leftC


    def insert_Right(self,value):
        if self.rightC==None:
            self.rightC=Tree(value)
        else:
            t=Tree(value)
            t.rightC=self.rightC
            self.rightC=t
        
        #return self.rightC
        
    
    def get_root(self):
        return self.root
    
    def get_rightC(self):
        return self.rightC
    
    def get_leftC(self):
        return self.leftC

    def set_root(self,new_root):
        self.root=new_root
        return self.root




    
root=Tree(3)


root.insert_Left(2)
root.insert_Left(1)
root.insert_Left(0)


root.set_root(4)

print(root.get_root())


root.insert_Right(5)
root.insert_Right(7)
root.insert_Right(9)


print(root.get_leftC().get_root())

print(root.get_rightC().get_root())


        