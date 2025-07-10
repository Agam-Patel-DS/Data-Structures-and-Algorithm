def findSingleAppearingElement(arr):
    xor=0
    for i in range(len(arr)):
        xor=xor^arr[i]

    return xor


arr=[4,1,2,1,2]
print(findSingleAppearingElement(arr))