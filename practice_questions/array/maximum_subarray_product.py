def subarray_product(arr):
    result=arr[0]
    maxending=arr[0]

    for i in range(1,len(arr)):
        maxending=max(maxending*arr[i],arr[i])
        result=max(result,maxending)
    return result

arr=[-2,6,-3,-10,0,2]
print(subarray_product(arr))