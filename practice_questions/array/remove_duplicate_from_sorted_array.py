#TBC

def placeOrder(arr,i):
    for j in range(i,len(arr)-1):
        arr[j]=arr[j+1]

    return arr

def removeDuplicatesFromArray(arr):
    if len(arr)==0 or len(arr)==1:
        return arr

    curUnique=-101
    prevUnique=-102
    prev=-101
    i = 0
    n = len(arr)

    for _ in range(n):
        if i >= len(arr):  # Break if index goes out of updated array
            break

        if arr[i] != prevUnique:
            curUnique = arr[i]

        if curUnique == prev:
            arr[i] = "_"
            arr = placeOrder(arr, i)
            arr[len(arr) - 1] = "_"
            continue  # stay at same index to check new element after shifting

        prevUnique = curUnique
        prev = curUnique
        i += 1

    return arr


arr = [1,1,2,3,4,4,4,4,4,4,5,5,5,6,6,6,6,7]
print(removeDuplicatesFromArray(arr))