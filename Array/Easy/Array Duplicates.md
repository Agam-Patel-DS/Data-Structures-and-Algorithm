# Array Duplicates
Difficulty: Easy Accuracy: 18.95% Submissions: 756K+ Points: 2
## Given an array arr of size n which contains elements in range from 0 to n-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1]. 

### Examples:
```
Input: n = 4, arr[] = [0,3,1,2]
Output: -1
Explanation: There is no repeating element in the array. Therefore output is -1.

Input: n = 5, arr[] = [2,3,1,2,3]
Output: 2 3 
Explanation: 2 and 3 occur more than once in the given array.
```
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:

- 1 <= n <= 105
- 0 <= arr[i] <= 105, for each valid i

## Solution

```
python

def counts(arr,n):
    unique=list(set(arr))      # list of uniquely present values in array
    repeated=[]       #list to store repeated elements
    flag=0         #to check whether any repeated elemen is present or not
    for i in range(0,len(unique)):     # for i = 0 to i=(lenght of unique -1)
        if arr.count(unique[i])>1:     # if count of elemen in unique is greater than 1 in arr
            repeated.append(unique[i])      # insert that element in repeated
            flag=1
    repeated.sort()    #sort the repeated value array
    
    if flag==1:
        return repeated
    if flag==0:
        return -1    
```
