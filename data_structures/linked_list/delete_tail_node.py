from common import Node, take_inputs, print_ll

# IMPORTANT!
# when we want to delete a node, we stop at a node before
# when we have to insert a node, we stop on the node where we will insert

def delete_tail(head):
    """
    parameter: head
    returns: head
    """
    if head==None or head.next==None: # empty linked list or single node
        return None
    temp=head
    while(temp.next.next!=None): # reaching second last node
        temp=temp.next
    temp.next=None # breaking the link between second last and last node
    return head # return head

def delete_tail_recursive(head):
    if head==None:
        return None
    if head.next==None:
        return None
    if head.next.next==None:
        head.next=None
        return head
    head.next=delete_tail_recursive(head.next)
    return head

head=take_inputs()
print_ll(head)
head=delete_tail(head)
print("\nAfter Deletion")
print_ll(head)
head=delete_tail_recursive(head)
print("\nAfter Deletion")
print_ll(head)