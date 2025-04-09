class stackUsingList:
    def __init__(self):
        self.__stack=[] # Very important to make it private

    def push(self,data):
        self.__stack.append(data)
        print(f"Pushed {data} into stack")

    def size(self):
        return len(self.__stack)
    
    def isEmpty(self):
        if len(self.__stack)==0:
            return True
        else:
            return False
    
    def top(self):
        if(self.isEmpty()):
            print("Error: Stack is Empty")
            return None
        return self.__stack[-1]
    
    def pop(self):
        return self.__stack.pop()



s=stackUsingList()
print(s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
print(s.isEmpty())
print(s.pop())
print(s.top())
print(s.isEmpty())
    
