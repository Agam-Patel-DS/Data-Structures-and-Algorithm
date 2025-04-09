# Remove all the duplicate values from the Linked List
# The Linked list is sorted
# Input: head
# Return: Linked List head without duplicates

from linked import *

def removeDuplicatesFromSortedLL(head):
    if head==None or head.next==None:
        return head
    
    temp=head
    
    while temp.next!=None:
        if temp.data==temp.next.data:
            temp.next=temp.next.next
        else:
            temp=temp.next

    return head

head=createLlFromList([1,2,2,3,4,4,5,6,7,7])
print_ll(head)
print("")
head=removeDuplicatesFromSortedLL(head)
print_ll(head)