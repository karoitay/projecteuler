#!/usr/bin/python


def solve_for(n):
  store_mod= False
  print "solving for", n
  l = [0]*n
  for i in xrange(n - 1, -1, -1):
    l[i] = 1
    for j in xrange(2*i + 1, n):
      l[j] += l[j - i - 1]
    if l[n - 1] > 1000000000:
      store_mod = True
    if (store_mod):
      for j in xrange(2*i + 1, n):
        l[j] %= 1000000
  try:
    return l.index(0) + 1
  except ValueError:
    return None

m = 1
n = None
while not n:
  m *= 2
  n = solve_for(m)
print n
