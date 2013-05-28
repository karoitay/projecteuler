#!/usr/bin/python
from fractions import gcd

MAX = 1000000

max_num = 0
max_val = 0
max_denom = 0
for denom in xrange(3, MAX + 1):
  num = int((3 * denom - 1) / 7)
  if float(num) / denom > max_val:
    max_val = float(num) / denom
    max_num = num
    max_denom = denom

# now to reduced form
d = gcd(max_num, max_denom)
while d != 1:
  max_num, max_denom = max_num / d, max_denom / d
  d = gcd(max_num, max_denom)
print max_num, "/", max_denom

