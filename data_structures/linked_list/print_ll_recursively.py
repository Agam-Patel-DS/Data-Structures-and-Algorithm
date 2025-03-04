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
    print(temp.data)
    print_ll(temp.next)

first = Node(4)
second = Node(3)
third = Node (1)
first.next=second
second.next=third
head=first

print_ll(head)
