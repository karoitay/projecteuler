#!/usr/bin/python
MAX_L = 1500000

# We will use Euclid's formual to generate all the relevant primitive Pythagoreans Triples.
# We need to find all comprime m,n where m>n and then: (m^2 - n^2, 2mn, m^2 + n^2) is a primitive triple.
# Note that if m > sqrt(MAX_L / 2) => m^2 > MAX_L / 2 => c = m^2 + n^2 > MAX_L / 2
# Also a + b > c => L = a + b + c > 2c and we will get L > MAX_L
# For this reason we will set MAX_M = floor(sqrt(MAX_L / 2))
from math import floor, sqrt
MAX_M = int(floor(sqrt(MAX_L / 2.0)))

def gcd(a, b):
  while b != 0:
    t = b
    b = a % t
    a = t
  return a

def triple(m, n):
  m_2, n_2 = m**2, n**2
  a, b, c = m_2 - n_2, 2 * m * n, m_2 + n_2
  if b < a:
    return (b, a, c)
  return (a, b, c)

def expand(a, b, c):
  ka, kb, kc = a, b, c
  l = ka + kb + kc
  while l <= MAX_L:
    yield (ka, kb, kc)
    ka, kb, kc = ka+a, kb+b, kc+c
    l = ka + kb + kc

#triples = set()
lengths = {}
for m in xrange(1, MAX_M + 1):
  for n in xrange((m % 2) + 1, m, 2):
    n_2 = n**2
    a, b, c = triple(m, n)
    l = a + b + c
    if gcd(m, n) == 1:
      for ka, kb, kc in expand(a, b, c):
        l = ka + kb + kc
        if not l in lengths:
          lengths[l] = set()
        lengths[l].add((ka, kb, kc))
print len([v for v in lengths.values() if len(v) == 1])
