stack=[]
def push():
    element=int(input("Enter the element to insert:"))
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed element:",e)
        print(stack)
def display():
    for i in stack:
        print(i,end=' ')
def peek():
    print(stack[-1])
def seek():
    h=0
    se=int(input("Enter the element to search:"))
    for i in range(len(stack)):
        if stack[i]==se:
            print("Element found at:",i)
            h=1
    if h==0:
        print("Element not found")
while True:
    print("\n1.push\n2.pop\n3.display\n4.peek\n5.seek\n6.exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        peek()
    elif ch==5:
        seek()
    elif ch==6:
        break
    else:
        print("Invalid choice")