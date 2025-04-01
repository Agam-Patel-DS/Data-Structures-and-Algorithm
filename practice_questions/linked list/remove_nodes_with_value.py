# Remove all nodes with value 'val'
# input: head, val
# return: head


from linked import *

def removeNodesWithValue(head,val):
    if head==None:
        return head
    if head.next==None:
        if head.data==val:
            return None
        else:
            return head
    
    temp=head
    newHead=head
    while temp.data==val and temp.next!=None:
        newHead=temp.next
        temp=temp.next

    while temp.next!=None:
        if temp.next.data==val:
            nextNode=temp.next.next
            temp.next=nextNode
        else:
            temp=temp.next


    if temp.next==None:
        if temp.data==val:
            temp=None

    return newHead



head=createLlFromList([1,2,3,4,5,3,3,4,5])
head2=createLlFromList([3,2,3,4,7,3])
head3=createLlFromList([])
head4=createLlFromList([1])

print_ll(head)
val=int(input("Enter the value to remove:"))
head=removeNodesWithValue(head,val)
print_ll(head)

print_ll(head2)
val=int(input("Enter the value to remove:"))
head2=removeNodesWithValue(head2,val)
print_ll(head2)

print_ll(head3)
val=int(input("Enter the value to remove:"))
head3=removeNodesWithValue(head3,val)
print_ll(head3)

print_ll(head4)
val=int(input("Enter the value to remove:"))
head4=removeNodesWithValue(head4,val)
print_ll(head4)