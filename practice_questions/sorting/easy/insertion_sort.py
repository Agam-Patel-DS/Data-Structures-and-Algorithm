# Insertion Sort Algorithm
def insertionSort(arr):
    n = len(arr)
    for current in range(1, n):
        currentCard = arr[current]
        correctPosition = current - 1

        # Shift elements of arr[0..current-1] that are greater than currentCard
        while correctPosition >= 0 and arr[correctPosition] > currentCard:
            arr[correctPosition + 1] = arr[correctPosition]
            correctPosition -= 1
        
        # Place the current element at the correct position
        arr[correctPosition + 1] = currentCard

    return arr


arr=[23,12,32,13,53,1]
print("Before Sorting: ",arr)
insertionSort(arr)
print("After Sorting: ",arr)