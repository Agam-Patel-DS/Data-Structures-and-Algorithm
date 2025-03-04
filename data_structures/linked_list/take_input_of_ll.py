#to do
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

    def details_of_a_single_node(self):
        print(f"Data: {self.data}\nNext: {self.next}")



def print_ll(head):
    if head==None:
        return
    temp=head
    # print_ll(temp.next) #print in reverse
    print(temp.data, end="-->")
    print_ll(temp.next)

def take_inputs():
    value=int(input("Enter the value: "))
    head=None
    
    while(value!=-1):
        newNode=Node(value)
        if(head==None):
            head=newNode

        else:
            temp=head
            while(temp.next!=None):
                temp=temp.next

            temp.next=newNode
        value=int(input("Enter the value: "))
    return head

head=take_inputs()
print_ll(head)
