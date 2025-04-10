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

def rotateDTimes(arr,D):
    if len(arr)==0 or len(arr)==1:
        return arr
    
    for i in range(D):
        arr=rotateOneStep(arr)

    return arr

arr=[1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]
print(rotateDTimes(arr,9))