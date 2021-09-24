def sumSquareDifference(n):
  l1 = [i**2 for i in range(1,n+1)]
  l2 = [i for i in range(1, n+1)]
  return sum(l2)**2 - sum(l1)
  
print (sumSquareDifference(100))
