#!/usr/bin/python
from utils.primes import get_primes

MAX = 100

primes_dict = get_primes(MAX)
primes = [i for i in xrange(2, MAX) if primes_dict[i]]
cache = {}
def update_answer(n, max_element=None):
  assert n >= 0, "n must be non-negative %d" % n
  if n == 0:
    return 1
  if n == 1:
    return 0
  max_element = min(n, max_element or n)
  if n in cache and max_element in cache[n]:
    return cache[n][max_element]
  count = 0
  i = 0
  while i < len(primes) and primes[i] <= max_element:
    p = primes[i]
    count += update_answer(n - p, min(p, max_element))
    i = i + 1
  cache_n = cache.get(n, {})
  cache_n[max_element] = count
  cache[n] = cache_n
  return count

for i in xrange(MAX):
  res = update_answer(i)
  if (res > 5000):
    print i
    break

