class Node:
    def __init__(self, value):
        self.data=value
        self.next=None

class queueUsingLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.len=0


    def size(self):
        return self.len
    
    def isEmpty(self):
        return self.size==0
    
    def enque(self,data):
        newNode=Node(data)
        self.len+=1
        if(self.head is None):
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        return f"Added {data} in the queue"
    
    def front(self):
        if self.isEmpty():
            print("Empty Queue")
            return

        return self.head.data
    
    def deque(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        self.len-=1
        dataReturned=self.head.data
        self.head=self.head.next
        if self.head==None: # Very Very Important to handle this 
            self.tail=None

        return dataReturned

queue=queueUsingLinkedList()
queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(5)
print(queue.size())
print(queue.isEmpty())
print(queue.front())
print(queue.deque())
print(queue.deque())
print(queue.deque())
print(queue.size())
print(queue.isEmpty())
print(queue.front())