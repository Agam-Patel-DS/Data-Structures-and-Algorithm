#TBC

def unionOfArrays(arr1,arr2):
    union=[]
    for i in range(len(arr1)-1):
        val=arr1[i]
        for j in range(len(arr2)-1):
            if arr2[j]==val:
                union.append(val)
    return union


arr1=[1,3,4,5,2,6,7]
arr2=[9,8,7,6,0,5,3]

print(unionOfArrays(arr1,arr2))
