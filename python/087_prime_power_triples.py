from utils.primes import getprimes

import math

MAX = 50000000

max_prime = int(math.sqrt(MAX))
primes = getprimes(max_prime)
primes = [p for p in primes if primes[p]]

found = set()
for p1 in primes:
  v1 = p1 ** 4
  if v1 >= MAX:
    break
  for p2 in primes:
    v2 = p2 ** 3
    if v1 + v2 >= MAX:
      break
    for p3 in primes:
      v3 = p3 ** 2
      v = v1 + v2 + v3
      if v >= MAX:
        break
      found.add(v)
print len(found)

