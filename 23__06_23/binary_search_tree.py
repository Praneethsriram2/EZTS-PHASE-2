class Node:
    def _init_(self,key):
        self.left=None
        self.key=key
        self.right=None

def insert(root,key):
    if root is None:
        return Node(key)
    if root.key==key:
        print("Duplicates are not allowed")
    elif root.key < key:
        root.right=insert(root.right,key)
    else:
        root.left=insert(root.left,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

root=None
while True:
    print("1.Insert\n2.Inorder Traversal\n3.Exit")
    ch=int(input("Enter YOur Choice:"))
    if ch==1:
        data=int(input("Enter Data to insert:"))
        root=insert(root,data)
    elif ch==2:
        print("Inoder Traversal:- ",end=' ')
        inorder(root)
        print()
    elif ch==3:
        print("\t*THE END*")
        break
    else:
        print("Invalid Choice")