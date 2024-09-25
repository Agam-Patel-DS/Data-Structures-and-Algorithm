## Given a number `num` and an array `arr`, find the number of pairs of the element of the array `arr` such that the sum of the numbers of the pairs is equal to `num`.
#### Constraints
  - No time or space complexity

### Solution:
```
num=10
arr=[1,4,7,2,8,9,6,0]
def twosum(arr, num):
    count=0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i]+arr[j]==num):
                count=count+1
                break
    return count
count=twosum(arr,num)
print(f"There are total {count} pairs.") #output should be 1+9, 2+8, 4+6 = 3
```
### Explaination
  - `len(arr)` : Length of array `arr`
  - `twosum(arr,num)` : The function to find the number of pairs.
