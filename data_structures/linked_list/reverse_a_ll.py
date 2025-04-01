from common import *

def reverseLL(head):
    if head is None or head.next is None:
        return head
    
    smallLinkedListHead=reverseLL(head.next)

    temp=smallLinkedListHead

    while(temp.next is not None):
        temp=temp.next


    temp.next=head
    head.next=None

    return smallLinkedListHead

# Time conplexity of above code --> O(n^2)

def reverseLLBetter(head):
    if head is None or head.next is None:
        return head
    
    smallLinkedListHead=reverseLL(head.next)

    tailOfReversedLL=head.next
    tailOfReversedLL.next=head
    head.next=None

    return smallLinkedListHead

def reverseLLIterative(head): # 3 Pointer Approach
    # p = Previous
    # c = Current
    # n = Next
    if head==None or head.next==None:
        return head
    
    prev=None
    current=head

    while current is not None:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node

    return prev


head=createLlFromList([1,2,3,4,5])
head=reverseLLIterative(head)
print_ll(head)