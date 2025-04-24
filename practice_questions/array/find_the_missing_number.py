# Find the missing number

def findTheMissingNubmer(arr:list):
    if len(arr)==0:
        return None
    
    sum=0
    maxNum=max(arr)
    for i in range(len(arr)):
        sum=sum+arr[i]

    exactSum=(maxNum*(maxNum+1))/2

    missingNumber=exactSum-sum
    return int(missingNumber)


arr=[9,6,4,2,3,5,7,0,1]
print("The missing number is: ", findTheMissingNubmer(arr))