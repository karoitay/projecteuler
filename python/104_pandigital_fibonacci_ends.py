#!/usr/bin/python
from math import log10,floor

def numlen(n):
  return int(log10(n)) + 1

def is_pandigital(n):
  s = set()
  while n != 0:
    s.add(n % 10)
    n /= 10
  return not 0 in s and len(s) == 9

def check(n):
  n_len = numlen(n)
  return n_len >= 9 and is_pandigital(n % 1000000000) and is_pandigital(n / (10 ** (n_len - 9)))

a, b = 1, 1
k = 3
n = a + b
while not check(n):
  a, b = b, n
  k += 1
  n = a + b
print k
