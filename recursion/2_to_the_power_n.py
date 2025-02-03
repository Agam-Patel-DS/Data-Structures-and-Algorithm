# recursive relation = 2^n = 2 x 2^(n-1)

def two_to_power_n(n:int):
  if n==0:
    return 1

  small_ans= two_to_power_n(n-1)
  ans= 2*small_ans

  return ans

number= int(input("Enter the n: ")) 
print(two_to_power_n(number))

# If n = 5, 2^5 = 2x2x2x2x2 = 32