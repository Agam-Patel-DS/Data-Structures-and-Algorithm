# Reverse a linked list
# Input: Head
# Return: Head

from linked import *
def reverseLL(head):
    """Creates and returns a reversed copy of the linked list."""
    new_head = None
    temp = head
    while temp:
        new_node = Node(temp.data)
        new_node.next = new_head
        new_head = new_node
        temp = temp.next
    return new_head

head=createLlFromList([1,2,3,4,5,])
print_ll(head)
print("")
head=reverseLL(head)
print_ll(head)