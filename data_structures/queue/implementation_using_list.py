class QueueUsingList:
    def __init__(self):
        self.__queue=[]

    def size(self):
        return len(self.__queue)
    
    def isEmpty(self):
        return self.size()==0
    
    def enque(self,data):
        self.__queue.append(data)
        return f"Appended {data}!"
    
    def front(self):
        if(self.size()==0):
            print(f"Empty Queue")
            return None
        return self.__queue[0]
    
    def deque(self):
        if(self.size()==0):
            print(f"Empty Queue")
            return None
        return self.__queue.pop(0)


queue=QueueUsingList()
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