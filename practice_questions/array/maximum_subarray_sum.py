def subarray_sum(arr):
    result=arr[0]
    maxending=arr[0]

    for i in range(1,len(arr)):
        maxending=max(maxending+arr[i],arr[i])
        result=max(result,maxending)
    return result

arr=[2,3,-8,7,-1,2,3]
print(subarray_sum(arr))