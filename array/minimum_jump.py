def minimum_jump(arr):
    pos=0
    jump=0
    length=len(arr)
    while pos<length-1:
        if arr[pos]==0:
            return -1
        else:
            jump+=1
            pos=pos+arr[pos]
    return jump

arr=[1,3,2]
print(minimum_jump(arr))