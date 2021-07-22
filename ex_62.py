#implementation of BST


class Node:
    
    def __init__(self,key):
        self.val=key
        self.right=None
        self.left=None


        

def insert(root,key):
    if root is None:
        return Node(key)
    
    else:
        if key==root.val:
            return root
        elif key>root.val:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
        
    return root



def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

        

root=Node(30)

root=insert(root,140)

root=insert(root,50)

#root.insert(root,Node(10))

#insert(root,Node(10))

#insert(root,Node(56))

#insert(root,Node(39))

#insert(root,Node(91))


(inorder(root))