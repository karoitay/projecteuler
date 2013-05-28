#!/usr/bin/python
MAX = 1000000

def phi(i, factors):
  for f in factors[i]:
    i *= ((f - 1) / float(f))
  return i

factors = {}
for i in xrange(2, MAX + 1):
  if i in factors:
    continue
  for j in xrange(i, MAX + 1, i):
    factors_j = factors.get(j, [])
    factors_j.append(i)
    factors[j] = factors_j

result = 0
for i in xrange(2, MAX + 1):
  result += phi(i, factors)
print int(result)

