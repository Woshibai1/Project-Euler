def Multiples(n,m):
  q = [i for i in range(0,1000) if i % n == 0 or i % m == 0]
  return sum(q)

print (Multiples(3,5))
