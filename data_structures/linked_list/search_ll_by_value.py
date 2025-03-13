from common import Node, take_inputs, print_ll, createLlFromList

def searchLlByValue(head,value):
    if head==None:
        return -1
    
    if head.data==value:
        return 0
    
    count=0
    temp=head
    while temp.data!=value and temp.next!=None:
        temp=temp.next
        count=count+1

    if temp.next==None and temp.data!=value:
        return -1
    
    if temp.next==None and temp.data==value:
        return count
    
    if temp.data==value:
        return count

def searchLlByValueBetter(head,value):
    temp=head
    index=0

    while temp!=None:
        if temp.data==value:
            return index
        temp=temp.next
        index+=1

    return "Not Found"


head=createLlFromList([0,1,2,3,4,5,6,7,8,9])
print_ll(head)
value=int(input("Enter the value to find: "))
index=searchLlByValue(head,value)
print("\nAfter Searching")
if index!=-1:
    print("The element ", value, "is present at index", index)
else:
    print("The element", value, "is not present in the Linked List")

value=int(input("Enter the value to find: "))
index=searchLlByValueBetter(head,value)
print("\nAfter Searching")
if index!=-1:
    print("The element ", value, "is present at index", index)
else:
    print("The element", value, "is not present in the Linked List")
