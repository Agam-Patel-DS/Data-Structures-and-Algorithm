from common import Node, take_inputs, print_ll

def insert_at_tail(head,value):
    newNode=Node(value)
    if head==None:
        print("Empty Linked List")
        return newNode
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=newNode
    return head

def insert_at_tail_recursive(head,value):
    temp=head
    if temp==None:
        newNode=Node(value)
        return newNode
    if temp.next==None:
        newNode=Node(value)
        temp.next=newNode
        return newNode
    newNode=insert_at_tail_recursive(temp.next,value)
    return head

def insert_at_tail_better(head,value):
    if head is None:
        newNode=Node(value)
        return newNode
    head.next=insert_at_tail_better(head.next,value)
    return head

head=take_inputs()
print_ll(head)
head=insert_at_tail(head,4)
print("\nAfter Inserting at tail")
print_ll(head)
head=insert_at_tail_recursive(head,4)
print("\nAfter Inserting at tail recursive")
print_ll(head)