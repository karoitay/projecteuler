#!/usr/bin/python
from collections import defaultdict
MAX = 10000000

def generate_devisors_count():
  devisors_sums = defaultdict(int)
  for d in xrange(2, MAX):
    for n in xrange(2*d, MAX, d):
      devisors_sums[n] += 1
  return devisors_sums

d = generate_devisors_count()
print sum(d[n] == d[n+1] for n in xrange(2, MAX-1))
