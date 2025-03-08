#to do
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

    def details_of_a_single_node(self):
        print(f"Data: {self.data}\nNext: {self.next}")


def print_ll(head):
    temp=head  #dont lose your head!!!
    while(temp!=None):
        print(temp.data,"-->",end="")
        temp=temp.next

    return
def take_inputs():
    value=int(input("Enter the value: "))
    head=None
    tail=None
    
    while(value!=-1):
        newNode=Node(value)
        if(head==None):
            head=newNode
            tail=newNode

        else:
            tail.next=newNode
            tail=newNode
            
        value=int(input("Enter the value: "))
    return head

def length(head):
    temp=head
    ans=0

    while(temp!=None):
        temp=temp.next
        ans+=1

    return ans

def insert_at_head(head,value):
    newNode=Node(value)
    newNode.next=head
    head=newNode
    return head

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
