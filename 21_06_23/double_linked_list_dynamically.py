#Double Linked List
class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def _init_(self):
        self.head=None
    def Insert_at_begin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            print(data,"inserted successfully")
            return
        self.head.prev=newnode
        newnode.next=self.head
        self.head=newnode
        print(data,"inserted at begin successfully")
        return
    def Insert_at_loc(self,data,loc):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            print(data,"inserted successfully")
            return
        if loc==1:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
            print(data,"inserted at location",loc,"successfully")
            return
        temp=self.head
        count=1
        while temp.next is not None and count+1!=loc:
            temp=temp.next
            count+=1
        if temp.next is None and count+1==loc:
            newnode.prev=temp
            temp.next=newnode
            print(data,"inserted at location",loc,"successfully")
            return
        if temp.next is not None:
            newnode.next=temp.next
            newnode.prev=temp
            temp.next=newnode
            temp=newnode.next
            temp.prev=newnode
            print(data,"inserted at location",loc,"successfully")
            return
        print("Enter valid location")
        return
    def Insert_at_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            print(data,"inserted successfully")
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
        print(data,"is inserted at end successfully")
        return
    def Delete_at_begin(self):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.head
        if self.head.next is None:
            print(self.head.data,"is deleted")
            self.head=None
            del(temp)
            return
        self.head=self.head.next
        self.head.prev=None
        print(temp.data,'is deleted')
        del(temp)
        return
    def Delete_at_middle(self,loc):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.head
        if self.head.next is None or loc==1:
            print(self.head.data,"is deleted")
            self.head=self.head.next
            del(temp)
            return
        ptr=None
        count=1
        while temp is not None and loc!=count:
            ptr=temp
            temp=temp.next
            count+=1
        if temp is None:
            print('Location out of range')
            return
        ptr.next=temp.next
        if temp.next is not None:
            temp.next.prev=ptr
        print(temp.data,'is deleted')
        del(temp)
        return
    def Delete_at_end(self):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.head
        if self.head.next is None:
            print(self.head.data,"is deleted")
            self.head=None
            del(temp)
            return
        ptr=None
        while temp.next is not None:
            ptr=temp
            temp=temp.next
        ptr.next=None
        print(temp.data,'is deleted')
        del(temp)
        return
    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.head
        print("List Elements are:",end=' ')
        while temp.next is not None:
            print(temp.data,end=' ')
            temp=temp.next
        print(temp.data)
        print("List Elements in reverse order:",end=' ')
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.prev
        print()
        return
l=DoubleLinkedList()
print('''1.Insert at begin\n2.Insert at Specified Posisiton\n3.Insert at end
4.Delete at Begin\n5.Delete at middle\n6.Delete at End
7.Display\n8.Exit''')
while True:
    ch=int(input("Enter your Choice:"))
    if ch==1:
        data=int(input("Enter data to insert:"))
        l.Insert_at_begin(data)
    elif ch==2:
        data=int(input("Enter data to insert:"))
        loc=int(input("Enter location to insert:"))
        l.Insert_at_loc(data,loc)
    elif ch==3:
        data=int(input("Enter data to insert:"))
        l.Insert_at_end(data)
    elif ch==4:
        l.Delete_at_begin()
    elif ch==5:
        loc=int(input("Enter Location:"))
        l.Delete_at_middle(loc)
    elif ch==6:
        l.Delete_at_end()
    elif ch==7:
        l.display()
    elif ch==8:
        print("\n\tTHE END\n")
        quit()
    else:
        print("\n\tINVALID ENTRY\n\tTRY ONCE AGAIN\n")