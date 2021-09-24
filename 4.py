def isPalindrome(n):
  l = list(str(n))
  if l == l[::-1]:
    return True
  else:
    return False

def biggestPalindrome():
  l = [i*g for i in range(100, 1000) for g in range(100, 1000)]
  l.sort(reverse=True)
  for i in l:
    if isPalindrome(i):
      return i
      
print(biggestPalindrome())
