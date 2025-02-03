# recursive relation = fact(n) = n x fact(n-1)

def factorial(n):
  if n<=1:
    return 1

  small_ans= factorial(n-1)
  ans= n*small_ans

  return ans


n=int(input("Enter the number: "))
print(factorial(n))
# If n = 4, the factoarial(4) = 4x3x2x1 = 24