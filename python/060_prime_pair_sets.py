#!/usr/bin/python
from utils.primes import get_primes
import math

MAX_P = 5000000

def isprime(n, primes, candidates):
  if n in primes:
    return primes[n]
  m = 0
  for c in candidates:
    if n % c == 0:
      primes[n] = False
      break
    if c > m:
      m = c
  if n in primes:
    return primes[n]
  m = m - (m % 6)
  s = int(math.sqrt(n)) + 1
  while m - 1 <= s:
    if n % (m - 1) == 0 or n % (m + 1) == 0:
      primes[n] = False
      break
    m = m + 6
  if not n in primes:
    primes[n] = True
  return primes[n]

def test(group, p, primes, candidates):
  for g in group:
    if not (isprime(g*(10**int(math.log(p,10) + 1)) + p, primes, candidates) and
      isprime(p*(10**int(math.log(g,10) + 1)) + g, primes, candidates)):
      return False
  return True


def extend(source, candidates, primes):
  result = []
  for g in source:
    m = max(g)
    for c in (i for i in candidates if i > m):
      if test(g, c, primes, candidates):
        result.append(g + [c])
  return result

def find(primes, candidates, size, found=None):
  if found == None:
    return find(primes, candidates, size, [[i] for i in candidates])
  while len(found) > 0 and len(found[0]) < size:
    found = extend(found, candidates, primes)
  return found

MAX = 9000
SIZE = 5
primes = get_primes(MAX_P)
candidates = [k for k,v in primes.iteritems() if k <= MAX and v]
print sum(find(primes, candidates, SIZE)[0])

