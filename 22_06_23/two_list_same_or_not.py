class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL1:
    def __init__(self):
        self.head=None
    def insert1(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            new=Node(data)
            new.next=self.head
            self.head=new
        print("Element inserted")
    def display1(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                if temp.next!=None:
                    print('->',end=' ')
                temp=temp.next
class LL2:
    def __init__(self):
        self.head=None
    def insert2(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            new=Node(data)
            new.next=self.head
            self.head=new
        print("Element inserted")
    def display2(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                if temp.next!=None:
                    print('->',end=' ')
                temp=temp.next
obj1=LL1()
obj2=LL2()
while 1:
    print("1.insert1\n2.insert2\n3.exit\n")
    ch=int(input("Enter choice:"))
    if ch==1:
        n=int(input("Enter data:"))
        obj1.insert1(n)
    elif ch==2:
        n=int(input("Enter data:"))
        obj2.insert2(n)
    elif ch==3:
        obj1.display1()
    elif ch==4:
        obj2.display2()
    elif ch==5:
        break
    else:
        print("Invalid choice")
