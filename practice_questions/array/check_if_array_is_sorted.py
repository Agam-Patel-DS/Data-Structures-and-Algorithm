#C
def isArraySorted(arr):
    if len(arr)==1 or len(arr)==0:
        return True
   
    next=-1
    previous=-1

    for i in range(len(arr)):
        next=arr[i]
        if next<previous:
            return False
        previous=next

    return True


arr=[]
print(isArraySorted(arr))