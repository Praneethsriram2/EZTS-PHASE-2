size=int(input("Enter the size of the array:\n"))
print("Enter the elements:\n")
l1=list(map(int,input().split()))
print(l1)
print("1.insert\n2.delete\n3.search\n4.sort5.exit\n")
while(True):
    ch=int(input("Enter the choice:"))
    if(ch==1):
        if(len(l1)>=size):
            print("Size is restricted:\n")
        else:
            n=int(input("Enter the element to insert:\n"))
            l1.append(n)
        print("List after adding:\n",l1)
    elif(ch==2):
        k=0
        delete=int(input("Enter the element to delete:\n"))
        for i in l1:
            if i==delete:
                l1.remove(i)
                k=1
        if k==1:
            print("List after deleting:\n",l1)
        else:
            print("Element not found:")
    elif(ch==3):
        se=int(input("Enter the element to search:\n"))
        for i in range(len(l1)):
            if l1[i]==se:
                print("Element found at location:",i)
            else:
                print("Element no found\n")
    elif(ch==4):
        l1.sort()
        print("Elements after sorting:/n",l1)
    elif(ch==5):
        break
    else:
        print("Invalid choice\n")