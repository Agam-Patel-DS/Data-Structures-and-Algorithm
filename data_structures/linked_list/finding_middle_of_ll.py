from common import *


headOdd=createLlFromList([1,2,3,4,5])
headEven=createLlFromList([1,2,3,4,5,6])

print_ll(headOdd)
print_ll(headEven)

# def middleOfLL(head):
#     if head is None or head.next is None:
#         return head
    
#     leng=length(head)

#     middle=leng//2

#     temp=head

#     count=0

#     while(count<middle):
#         temp=temp.next
#         count+=1

#     return temp


## Two Pointer Approach: Fast and Slow Pointer --- 
#  Fast pointer will be twice faster than the slow one, 
#  so when the faster one will be reaching end, the slow 
#  one will reach the half of the linked list.

def middleOfLL(head):
    if head is None or head.next is None:
        return head
    
    slow=head
    fast=head

    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next

    return slow



headOddMid=middleOfLL(headOdd)
headEvenMid=middleOfLL(headEven)
print("")
print(headOddMid.data)
print(headEvenMid.data)
