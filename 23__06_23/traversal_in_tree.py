class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=' ')
        inorder(root.right)
def preorder(root):
    if root:
        print(root.val,end=' ')
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=' ')
root=Node(100)
root.left=Node(400)
root.right=Node(500)
root.left.left=Node(700)
root.left.right=Node(600)
root.left.right.left=Node(900)
root.right.left=Node(800)
root.right.right=Node(200)
root.right.right.left=Node(300)
print("inorder is:",end=' ')
inorder(root)
print("\npreorder is:",end=' ')
preorder(root)
print("\nPostorder is:",end=' ')
postorder(root)