# Find the value of the middle node of the linked list
# If there are two nodes, then return the second one
# Input: The head node
# Return: middle node of the linked list

from linked import *

def findMiddleNode(head):
    if head==None:
        return head
    if head.next==None:
        return head.data
    
    slow=head
    fast=head

    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next

    if fast.next==None:
        return slow.data
    else:
        return slow.next.data



head=createLlFromList([1,2,3,4,5,6,7,8,9])
head2=createLlFromList([1,2,3,4,7,8])
head3=createLlFromList([])
head4=createLlFromList([1])

print_ll(head)
value=findMiddleNode(head)
print(f"The value at the middle node of the linked list is {value}")

print_ll(head2)
value1=findMiddleNode(head2)
print(f"The value at the middle node of the linked list is {value1}")

print_ll(head3)
value2=findMiddleNode(head3)
print(f"The value at the middle node of the linked list is {value2}")

print_ll(head4)
value3=findMiddleNode(head4)
print(f"The value at the middle node of the linked list is {value3}")