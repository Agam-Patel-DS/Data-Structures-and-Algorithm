# Bubble Sort Algorithm
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

def bubbleSortRecursive(arr, s):
    if s >= len(arr) - 1:
        return

    for j in range(len(arr) - 1 - s):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    bubbleSortRecursive(arr, s + 1)

arr=[23,12,22,13,53,1]
print("Before Sorting: ",arr)
bubbleSortRecursive(arr,0)
print("After Sorting: ",arr)