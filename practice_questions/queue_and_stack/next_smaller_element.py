def find_right_smaller(a, n, i):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            return a[j]
    return -1

def next_smaller(a, n):
    if n == 0:
        return -1
    if n == 1:
        return [-1]

    ans = []
    for i in range(n):
        ans.append(find_right_smaller(a, n, i))
    return ans

sample=[4, 5, 2, 10, 8]
print(next_smaller(sample,5))