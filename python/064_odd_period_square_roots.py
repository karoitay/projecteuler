import math

def getnext(n, a, b, intsqrtn):
  r = int((intsqrtn+a)/b)
  a0 = r*b - a
  b0 = (n - a0*a0)/b
  return (r, a0, b0)

def getperiod(n):
  intsqrtn = int(math.sqrt(n))
  if intsqrtn**2 == n:
    return None
  i, a, b = 0, 0, 1
  d = {}
  while True:
    r, a, b = getnext(n, a, b, intsqrtn)
    k = (a, b)
    if k in d:
      return i - d[k]
    d[k] = i
    i = i + 1
  return None

MAX = 10000
count = 0
for i in range(2, MAX + 1):
  p = getperiod(i)
  if p != None and p % 2 == 1:
    count = count + 1
print count
