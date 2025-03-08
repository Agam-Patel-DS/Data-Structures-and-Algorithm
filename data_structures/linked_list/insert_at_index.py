from common import Node, take_inputs, print_ll, insert_at_head


def insert_at_index(head, data, index):
    if index==0:
        return insert_at_head(head, data)
    
    newNode=Node(data)
    temp=head
    count=0

    while temp is not None and count < index - 1:
        temp = temp.next
        count+=1

    if temp == None:
        print("Linked List Out Of Index")
        return head
    
    newNode.next=temp.next
    temp.next = newNode
    return head

def insert_at_index_recursive(head, value, index, count=0): #personal
    if head==None:
        return head
    
    if index==0:
        return insert_at_head(head, value)
    
    temp=head

    if head is not None and count == index -1:
        newNode=Node(value)
        newNode.next=temp.next
        temp.next=newNode
        return head
    insert_at_index_recursive(temp.next,value,index,count+1)

    return head

def insert_at_index_recursive_better(head,data,index): #course
    if index==0:
        return insert_at_head(head,data)
    if head==None:
        print("Index Out of Bound!")
        return head
    head.next=insert_at_index_recursive_better(head.next,data,index-1)
    return head

value=1
head=take_inputs()
print_ll(head)
value=value+1
head=insert_at_index(head,value,3)
print("\n")
print_ll(head)
value=value+1
head=insert_at_index_recursive(head,value,3)
print("\n")
print_ll(head)
value=value+1
head=insert_at_index_recursive_better(head,value,3)
print("\n")
print_ll(head)