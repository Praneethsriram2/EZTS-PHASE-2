queue=[]
def enqueue():
    element=int(input("Enter the element to insert:"))
    queue.append(element)
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("Removed element:",e)
        print(queue)
def display():
    for i in queue:
        print(i,end=' ')
def seek():
    h=0
    se=int(input("Enter the element to search:"))
    for i in range(len(queue)):
        if queue[i]==se:
            print("Element found at:",i)
            h=1
    if h==0:
        print("Element not found")
while True:
    print("\n1.enqueue\n2.dequeue\n3.display\n4.seek\n5.exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        seek()
    elif ch==5:
        break
    else:
        print("Invalid choice")