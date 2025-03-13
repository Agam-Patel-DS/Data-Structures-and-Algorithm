def minimize_the_height(arr,k):
    maxi=max(arr)
    mini=min(arr)
    min_index=-1
    max_index=-1
    for i in range(len(arr)):
        if arr[i]==mini:
            arr[i]=arr[i]+k
            min_index=i
        elif arr[i]==maxi and arr[i]>k:
            arr[i]=arr[i]-k
            max_index=i
        elif arr[i]==maxi and arr[i]<k:
            arr[i]=arr[i]+k
            max_index=i
        else:
            arr[i]=arr[i]+k
    return abs(arr[max_index]-arr[min_index])


k=1
arr=[2,3]
print(minimize_the_height(arr,k))