from utils.primes import getprimes

import math
MAX = 10**7
HIGH_BOUND = int(math.sqrt(MAX) * 2)

def permutations(n1, n2):
  l1, l2 = list(str(n1)), list(str(n2))
  if len(l1) != len(l2):
    return False
  for c in l1:
    if not c in l2:
      return False
    l2.remove(c)
  return len(l2) == 0

primes = getprimes(HIGH_BOUND)
primes = [i for i in xrange(2, HIGH_BOUND) if primes[i]]

result = 0
max_found = 0
for p1 in primes:
  for p2 in primes:
    if p1 == p2 or p1 * p2 >= MAX:
      continue
    n, phi_n = p1 * p2, (p1 - 1) * (p2 - 1)
    if not permutations(n, phi_n):
      continue
    if float(phi_n) / n > max_found:
      max_found = float(phi_n) / n
      result = n
print result

