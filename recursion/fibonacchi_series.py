def fibonacchi_series(n:int):

  if n<=1:
    return 1

  ans_1= fibonacchi_series(n-1)
  ans_2= fibonacchi_series(n-2)

  final_ans = ans_1 + ans_2

  return final_ans


number = 5
print(fibonacchi_series(number))
# The answer should be: 1, 1, 2, 3, 5, 8
  