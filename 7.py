import math
def is_prime(n):
  l = []
  g = 1
  while len(l) < n:
    g += 1
    if all(g % i != 0 for i in range(2, int(math.sqrt(g))+1)):
      l.append(g)  
  return l[-1]
    
print(is_prime(10001))
