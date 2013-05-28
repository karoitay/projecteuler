#!/usr/bin/python
from decimal import *

MAX = 100
INTEGRAL_ROOTS = set([1, 4, 9, 16, 25, 36, 49, 64, 81])
getcontext().prec = 105
result = 0
for i in xrange(2, 100):
  if not i in INTEGRAL_ROOTS:
    s = str(Decimal(i).sqrt()).split('.')
    result += int(s[0]) + sum([int(c) for c in s[1][0:99]])
print result

