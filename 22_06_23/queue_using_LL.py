class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class queue():
    def __init__(self):
        self.head=None
    def enqueue(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(data)
        print("Data inserted Successfull")
        print("Insert at end operations completed successfully")
    def dequeue(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            self.head=self.head.next
            print(temp.data,"is deleted successfully")
            del(temp)
        print("Delete operation is completed successfully")
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
obj=queue()
while True:
    print("\n1.enqueue\n2.dequeue\n3.display\n4.exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        ele=int(input("enter the data:"))
        obj.enqueue(ele)
    elif ch==2:
        obj.dequeue()
    elif ch==3:
        obj.display()
    elif ch==4:
        break
    else:
        print("Invalid choice")