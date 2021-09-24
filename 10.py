import math
def summationOfPrimes(n):
  l = []
  g = 1
  while g < n:
    g += 1
    if all(g % i != 0 for i in range(2, int(math.sqrt(g))+1)):
      l.append(g)  
  return sum(l)
    
print(summationOfPrimes(2000000))
