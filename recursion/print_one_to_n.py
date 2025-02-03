# recursive relation: print(1 to n) = print(1)+print(2 to n)

def print_one_to_n(n:int):

  if(n<1):
    return

  print_one_to_n(n-1)
  print(n)

n= int(input("Enter the n: "))
print_one_to_n(n)