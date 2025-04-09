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
        print(temp.data,"--> ",end="")
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

def delete_head(head):
    """
    parameter: head
    returns: head
    """
    if head==None or head.next==None:
        return None
    newhead=head.next
    return newhead

def delete_tail(head):
    """
    parameter: head
    returns: head
    """
    if head==None or head.next==None: # empty linked list or single node
        return None
    temp=head
    while(temp.next.next!=None): # reaching second last node
        temp=temp.next
    temp.next=None # breaking the link between second last and last node
    return head # return head


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

def createLlFromList(l1):
    head=None
    tail=None
    for value in l1:
        newNode=Node(value)
        if head==None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode

    return head

def length(head):
    temp=head
    ans=0

    while(temp!=None):
        temp=temp.next
        ans+=1

    return ans

def reverseLL(head):
    """Creates and returns a reversed copy of the linked list."""
    new_head = None
    temp = head
    while temp:
        new_node = Node(temp.data)
        new_node.next = new_head
        new_head = new_node
        temp = temp.next
    return new_head