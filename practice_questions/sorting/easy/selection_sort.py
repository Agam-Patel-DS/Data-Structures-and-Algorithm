# Selection Sort Algorithm
def selectionSort(arr):
    length=len(arr)
    for i in range(length-1):
        minIndex=i
        for j in range(i+1,length):
            if (arr[j]<arr[minIndex]):
                minIndex=j

        arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr




# Driver Code
arr=[23,1,31,4,0,6,5]
print(f"Before Sorting: {arr}")
selectionSort(arr)
print(f"After Sorting: {arr}")