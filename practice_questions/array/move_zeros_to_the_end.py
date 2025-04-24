# TBC

def moveZerosToEnd(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    
    length=len(arr)-1
    check=0
    zeros=0
    for i in range(len(arr)-1):
        if arr[i]==0:
            zeros=zeros+1

    for i in range(len(arr)-1):
        if arr[i]==0 and check!=zeros:
            check=check+1
            for j in range(i,len(arr)-1):
                arr[j]=arr[j+1]
            arr[length]=0
            length=length-1
        
    return arr


arr=[]
print(moveZerosToEnd(arr))