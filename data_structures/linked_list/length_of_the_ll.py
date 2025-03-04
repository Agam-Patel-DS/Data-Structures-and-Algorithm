from common import Node, take_inputs, print_ll
def length(head):
    temp=head
    ans=0

    while(temp!=None):
        temp=temp.next
        ans+=1

    return ans

def length_recursive(head):
    temp=head

    if temp==None:
        return 0
    
    smallans=length_recursive(temp.next)
    ans= 1+smallans

    return ans

head=take_inputs()
print_ll(head)
print("\n",length(head))
print("\n",length_recursive(head))
