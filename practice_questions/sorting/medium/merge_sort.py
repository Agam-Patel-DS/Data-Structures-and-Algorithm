def merge(l1, s, m, e):
    i = s
    j = m + 1
    ans = []

    # Merging two sorted halves
    while i <= m and j <= e:
        if l1[i] < l1[j]:
            ans.append(l1[i])
            i += 1
        else:
            ans.append(l1[j])
            j += 1

    # Append remaining elements from the left half
    while i <= m:
        ans.append(l1[i])
        i += 1

    # Append remaining elements from the right half
    while j <= e:
        ans.append(l1[j])
        j += 1

    # Copy sorted elements back into original list
    l1[s:e+1] = ans  


def merge_sort_helper(l1, s, e):
    if s >= e:
        return  

    mid = s + (e - s) // 2  

    # Recursively divide the array
    merge_sort_helper(l1, s, mid)
    merge_sort_helper(l1, mid + 1, e)

    # Merge the sorted halves
    merge(l1, s, mid, e)


def merge_sort(l1):
    merge_sort_helper(l1, 0, len(l1) - 1)  #  No return needed

arr=[10,9,8,7,5,4,3,2,1]
merge_sort(arr)
print(arr)