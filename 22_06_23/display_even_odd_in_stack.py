stack=[]
def push():
    element=int(input("Enter the element to insert:"))
    stack.append(element)
    print(stack)
def pop():
    stack.pop()
    print(stack)
def even():
    print("Even numbers are:")
    for i in stack:
            if(i%2==0):
                print(i,end=' ')
    print()
def odd():
    print("odd numbers are:")
    for i in stack:
        if i%2!=0:
            print(i,end=' ')
    print()
while 1:
    print("1.push\n2.pop\n3.even\n4.odd\n5.exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        push()
    if ch==2:
        pop()
    elif ch==3:
        even()
    elif ch==4:
        odd()
    elif ch==5:
        print("___The_End___")
        break
    else:
        print("invalid choice")