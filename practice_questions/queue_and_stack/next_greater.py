# Input is an array having integers: [1,2,3,4] and number/ingeter n having length of array: 4
# Output: [2,3,4,-1]
# Greater element should be on the right
# Last element will always have -1
# If there is no greater number on the right then -1

def find_right_greater(a, n, i):
    for j in range(i + 1, n):
        if a[j] > a[i]:
            return a[j]
    return -1

def next_greater(a, n):
    if n == 0:
        return -1
    if n == 1:
        return [-1]

    ans = []
    for i in range(n):
        ans.append(find_right_greater(a, n, i))
    return ans

# Test
sample_array = [1, 3, 2, 4]
n = len(sample_array)
print(next_greater(sample_array, n))  # Output: [3, 4, 4, -1]
