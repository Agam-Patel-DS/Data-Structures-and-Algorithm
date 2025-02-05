# Merge Sort
def merge(l1,s,m,e):
  pass

def merge_sort_helper(l1,s,e):
  if (s>=e):
    return

  mid=s+(e-s)//2

  merge_sort_helper(l1,s,mid)
  merge_sort_helper(l1,mid+1,e)

  merge(l1,s,mid,e)
  return

def merge_sort(l1):
  return merge_sort_helper(l1,0,len(l1))

l1=[23,54,12,52,65,21]
print(merge_sort(l1))