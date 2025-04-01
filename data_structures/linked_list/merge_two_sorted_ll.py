from common import *


ll1=createLlFromList([5])
ll2=createLlFromList([3,6])

## Warning: Make sure to handle the 'None' properly.
def mergeTwoSortedLL(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    finalHead=None
    finalTail=None

    while head1 is not None and head2 is not None:
        if head1.data<head2.data:
            if finalHead is None:
                finalHead=head1
                finalTail=head1
            else:
                finalTail.next=head1
                finalTain=head1
            head1=head1.next
        else:
            if finalHead is None:
                finalHead=head2
                finalTail=head2
            else:
                finalTail.next=head2
                finalTail=head2
            head2=head2.next
    
    if head1 is not None:
        finalTail.next=head1

    if head2 is not None:
        finalTail.next=head2

    return finalHead


finalhead=mergeTwoSortedLL(ll1,ll2)
print_ll(finalhead)
