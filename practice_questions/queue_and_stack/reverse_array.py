class Stack:
    def __init__(self):
        self._stack=[]

    def push(self,value):
        self._stack.append(value)

    def length(self):
        return len(self._stack)
    
    def pop(self):
        if self.length()==0:
            return "Empty stack"
        return self._stack.pop()
    
    def top(self):
        if self.length()==0:
            return "Empty stack"
        return self._stack[-1]
    
    def isEmpty(self):
        return len(self._stack)==0
    

def reverseArray(array):
    if len(array)==0 or len(array)==1:
        return array
    stack=Stack()
    l=len(array)
    for i in range(0,l):
        stack.push(array[i])

    final_array=[]
    while stack.length()!=0:
        value=stack.pop()
        final_array.append(value)
    return final_array


sample_array=[8,9]
print(reverseArray(sample_array))


    