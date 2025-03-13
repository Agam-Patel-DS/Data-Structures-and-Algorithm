# Bubble Sort Algorithm
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

arr=[23,12,32,13,53,1]
print("Before Sorting: ",arr)
bubbleSort(arr)
print("After Sorting: ",arr)