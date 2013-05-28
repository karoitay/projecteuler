#!/usr/bin/python
_MOD = 10**10
_A = 28433
_B = 7830457

# Need to find the last 10 digits of _A*(2**_B) + 1
r = _A
for i in xrange(_B):
  r = (r << 1) % _MOD
r = (r + 1) % _MOD
print r

