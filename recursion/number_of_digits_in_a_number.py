# recursive function: digits(n) = 1+digits(n//10)

def number_of_digits(n:int):

  if n//10==0:
    return 1

  small_ans=number_of_digits(n//10)
  ans = 1+small_ans

  return ans


n = int(input("Enter the n: "))
print(number_of_digits(n))

# If n = 4546, then digits(4546) = 4