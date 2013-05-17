from math import floor
from math import ceil
from fractions import gcd

MAX = 12000

count = 0
for denom in xrange(3, MAX + 1):
  a = int(ceil((denom + 1) / 3.0))
  b = (denom - 1) / 2
  for num in xrange(a, b + 1):
    if gcd(num, denom) == 1:
      count = count + 1
print count

