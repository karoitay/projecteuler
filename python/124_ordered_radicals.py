#!/usr/bin/python

from collections import defaultdict
from operator import mul

def rad(max):
  rad = defaultdict(lambda: 1)
  rad[1] = 1
  for i in xrange(2, max + 1):
    if i in rad:
      continue
    for j in xrange(i, max + 1, i):
      rad[j] *= i
  return rad

def E(rad, x):
  reverese_rad = defaultdict(set)
  for k, v in rad.iteritems():
    reverese_rad[v].add(k)

  cnt = 0
  for rad_n in sorted(reverese_rad.keys()):
    vals = reverese_rad[rad_n]
    cnt += len(vals)
    if cnt < x:
      continue
    return [n for n in sorted(vals)][x - cnt + len(vals) - 1]

MAX = 100000
X = 10000
print E(rad(MAX), X)
