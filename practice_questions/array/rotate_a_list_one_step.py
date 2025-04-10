# TBC

def rotateOneStep(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    

    end=arr[len(arr)-1]
    next=arr[1]
    prev=arr[0]

    for i in range(1,len(arr)-1):
        arr[i]=prev
        prev=next
        next=arr[i+1]

    arr[len(arr)-1]=prev
    arr[0]=end

    return arr

arr=[1,2]
print(rotateOneStep(arr))