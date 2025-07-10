def isOperator(stack,operation):
    value1=stack[-1]
    value2=stack[-2]
    if operation=="+":
        return value2+value1
    elif operation=="-":
        return value2-value1
    elif operation=="*":
        return value2*value1
    elif operation=="/":
        return int(value2/value1)
    else:
        return "Error"

def evaluatePostfix(array):
    if len(array)==0 or len(array)==1:
        return array
    stack=[]
    for exp in array:
        if exp=="+" or exp=="-" or exp=="*" or exp=="/":
            value=isOperator(stack,exp)
            stack.pop()
            stack.pop()
            stack.append(value)
        else:
            stack.append(int(exp))
    return stack[-1]

sample=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evaluatePostfix(sample))