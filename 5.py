import math
def leastMultiple(m,n):
  answer = 1
  for i in range(m, n):
    answer *= i // math.gcd(i, answer)
  return answer

print(leastMultiple(1,20))
