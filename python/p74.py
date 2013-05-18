from math import factorial
F = [factorial(i) for i in xrange(10)]

def f(n):
  if n == 0:
    return 1
  s = 0
  while n != 0:
    s += factorial(n % 10)
    n = n / 10
  return s

def update_cache_for(n, cache):
  if not n in cache:
    f_n = f(n)
    if f_n == n:
      cache[n] = 1
    else:
      cache[n] = 1 + update_cache_for(f_n, cache)
  return cache[n]

cache = {169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2}
for n in range(1000000):
  update_cache_for(n, cache)
print len([i for i in cache if cache[i] == 60])

