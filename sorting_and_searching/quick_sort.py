def partitionFunction(l1, s, e):
    pivot = l1[e]

    i = s
    rightPosition = s 

    while i <= e - 1:
        if l1[i] < pivot:
            l1[rightPosition], l1[i] = l1[i], l1[rightPosition] 
            rightPosition += 1  
        i += 1

    l1[rightPosition], l1[e] = l1[e], l1[rightPosition]  

    pivotIndex = rightPosition  

    start = s
    end = e

    while start < pivotIndex and end > pivotIndex:
        if l1[start] < pivot:
            start += 1
        elif l1[end] >= pivot:
            end -= 1
        else:
            l1[start], l1[end] = l1[end], l1[start]
            start += 1
            end -= 1

    return pivotIndex  

def QuickSort(l1, s, e):
    if s >= e:
        return

    pivotIndex = partitionFunction(l1, s, e)

    QuickSort(l1, s, pivotIndex - 1)
    QuickSort(l1, pivotIndex + 1, e)

# Test the function
l1 = [3, 6, 7, 2, 1, 4, 5]
QuickSort(l1, 0, len(l1) - 1)
print(l1)  # Expected Output: [1, 2, 3, 4, 5, 6, 7]
