from common import Node, take_inputs, print_ll, createLlFromList

def iterativeSearchLlByIndex(head,index):
    temp=head
    count=0
    while count<index and temp!=None:
       temp=temp.next
       count=count+1
     
    if temp==None:
        return -1
    
    else:
        return temp.data
    

head=createLlFromList([])
print_ll(head)
value=int(input("Enter the index to find: "))
index=iterativeSearchLlByIndex(head,value)
print("\nAfter Searching")
if index!=-1:
    print("The element ", value, "is present at index", index)
else:
    print("The element", value, "is not present in the Linked List")
