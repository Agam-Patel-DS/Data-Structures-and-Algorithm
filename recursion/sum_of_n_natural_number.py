# recursive relation : sum(n)= n+sum(n-1)

def sum_of_n_natural_numbers(n:int):

  if n==1:
    return 1

  small_ans=sum_of_n_natural_numbers(n-1)
  ans= n + small_ans

  return ans

n= int(input("Enter the n: "))
print(sum_of_n_natural_numbers(n))

# If n = 10, then sum(10)= 1+2+3+4+5+6+7+8+9+10 = 55