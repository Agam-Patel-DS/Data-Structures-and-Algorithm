def binary_search(l1,x,s,e):

  if s>e:
    return False

  mid = s+(e-s)//2

  if(l1[mid]==x):
    return True

  if(l1[mid]>x):
    return binary_search(l1,x,s,mid-1)
  return binary_search(l1,x,mid+1,e)

l1=[12,23,43,65,76,87,98]
print(binary_search(l1,76,0,len(l1)-1))