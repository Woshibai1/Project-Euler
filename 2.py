def EvenFibonacciNumbers(n):
  list = [1,2]
  result = 0
  while True:
    nf = list[-1]+list[-2]
    if nf% 2 == 0 and nf >= n:
      for i in list:
        if i %2 == 0:
          result += i
      return result
    else:
      list.append(nf)

print(EvenFibonacciNumbers(4000000))
