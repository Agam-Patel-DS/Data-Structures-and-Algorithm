# Code a function which finds the first node with value k
# If no such node, return -1
# Input: head, k
# Return: index of node or -1

from linked import *

def nodeWithValueK(head,k):
    # If the linked list is empty
    if head==None:
        return -1
    # If the linked list is having only one node
    if head.next==None:
        if head.data==k:
            return 0
        else:
            return -1
    # If linked list is haing more than one nodes
    temp=head
    count=0
    while temp.data!=k and temp.next!=None:
        temp=temp.next
        count=count+1

    if temp.next==None:
        return -1
    
    return count


# Driver Program
head=createLlFromList([])
print_ll(head)
k=int(input("Enter the value you want to find:"))
index=nodeWithValueK(head,k)
print(f"The index of element is: {index}")