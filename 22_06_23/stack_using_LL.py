class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class stack():
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            new=Node(data)
            new.next=self.head
            self.head=new
        print("Element inserted successfully")
    def pop(self):
        if self.head is None:
            print("List is empty")
        else:
            print("popped element is:",self.head.data)
            self.head=self.head.next
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                if temp.next!=None:
                    print('->',end=' ')
                temp=temp.next
        print("\nDisplay operation completed successfully")
obj=stack()
while True:
    print("\n1.push\n2.pop\n3.display\n4.exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        ele=int(input("enter the data:"))
        obj.push(ele)
    elif ch==2:
        obj.pop()
    elif ch==3:
        obj.display()
    elif ch==4:
        break
    else:
        print("Invalid choice")