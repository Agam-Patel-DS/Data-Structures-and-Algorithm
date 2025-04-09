# TBC
def largestElemenet(arr):
    if len(arr)==1:
        return arr[0]
    if len(arr)==0:
        return None
    largest=-1
    for i in range(len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    
    return largest


arr=[]
print(largestElemenet(arr))