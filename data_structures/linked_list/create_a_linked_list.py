# create a node of LL

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

    def details(self):
        print(f"Data: {self.data}\nNext: {self.next}")


first = Node(4)
second = Node(3)
third = Node (1)
third.details()

print(id(first), id(second), id(third))

first.next=second
second.next=third

first.details()
second.details()
third.details()
print(first.next.data) #prints the data of second

head=first
print(head.data)
print(head.next.data)
print(head.next.next.data)