def majority_element(arr):
    pass
    count={}
    majority=len(arr)//2
    for num in arr:
        count[num]=count.get(num,0)+1
        if count[num]>majority//2:
            return num
    return -1


            

arr=[3,1,3,3,2]
print(majority_element(arr))