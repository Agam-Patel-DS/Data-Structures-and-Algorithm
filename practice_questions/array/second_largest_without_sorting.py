#TBC

def secondLargestWithoutSorting(arr):
    if len(arr)==0:
        return None
    if len(arr)==1:
        return -1
    
    largest=-1
    secondLargest=-1

    for i in range(len(arr)):
        if arr[i]>largest:
            if secondLargest!=largest:
                secondLargest=largest
            largest=arr[i]

        if arr[i]<largest and arr[i]>secondLargest:
            secondLargest=arr[i]
    
    return secondLargest

arr=[]
print(secondLargestWithoutSorting(arr))