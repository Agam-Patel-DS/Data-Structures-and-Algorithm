from common import Node, take_inputs, print_ll


def delete_head(head):
    """
    parameter: head
    returns: head
    """
    if head==None or head.next==None:
        return None
    newhead=head.next
    return newhead

head=take_inputs()
print_ll(head)
head=delete_head(head)
print("\nAfter Deletion")
print_ll(head)