from common import Node, take_inputs, print_ll

def deleteNodeByValue(head,value):
    if head==None:
        return None
    
    temp=head

    while  temp.next!=None and temp.next.data!=value:
        temp=temp.next

    if temp.data!=value and temp.next==None:
        print("Value Not Found")
        return head
    
    if temp.data==value and temp.next==None:
        return None
    
    else:
        nextNode=temp.next
        temp.next=nextNode.next
    return head

def deleteNodeByValueRecursive(head, value):
    if head==None:
        print("Value Not Found")
        return None
    
    if head.data==value:
        return head.next
    
    head.next=deleteNodeByValueRecursive(head.next,value)
    return head

head=take_inputs()
print_ll(head)

index=int(input("Enter the value to delete: "))
head=deleteNodeByValue(head,index)
print("\nAfter Deletion")
print_ll(head)

index=int(input("Enter the value to delete: "))
head=deleteNodeByValueRecursive(head,index)
print("\nAfter Deletion")
print_ll(head)