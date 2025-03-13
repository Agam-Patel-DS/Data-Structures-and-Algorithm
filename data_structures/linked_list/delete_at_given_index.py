from common import Node, take_inputs, print_ll, delete_head, delete_tail

# IMPORTANT!
# when we want to delete a node, we stop at a node before
# when we have to insert a node, we stop on the node where we will insert

def delete_at_index(head,index):
    """
    parameter: head
    returns: head
    """
    if index==0:
        return delete_head(head) # if the first element to be deleted
    
    temp=head
    count=0

    while(temp is not None and count<index-1): # to get at the required index
        temp=temp.next
        count+=1

    if temp==None: # check if the index is greater than the length of the LL
        print("Index out of range")
        return head
    
    if temp.next==None: # check of the next of last node
        print("Index out of range")
        return head
    
    temp.next=temp.next.next # deleting the node
    print(f"delete at index {index}")

    return head
    
def delete_at_index_recursive(head,index):
    if head==None:
        print("Index Out of Bounds")
        return None
    if index==0:
        return head.next

    head.next=delete_at_index_recursive(head.next,index-1)
    return head

head=take_inputs()
print_ll(head)
index=int(input("Enter the index to delete: "))
head=delete_at_index(head,index)
print("\nAfter Deletion")
print_ll(head)
index=int(input("Enter the index to delete: "))
head=delete_at_index_recursive(head,index)
print("\nAfter Deletion")
print_ll(head)