from common import Node, print_ll, take_inputs, length

def insert_at_head(head, value):
    newNode=Node(value)
    newNode.next=head
    head=newNode
    return head

head=take_inputs()
print_ll(head=head)
head=insert_at_head(head)
print_ll(head=head)