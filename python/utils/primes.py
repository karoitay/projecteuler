def get_primes(n):
  """Computes all the prime numbers up to and not including n

  Args:
    n: the upper bound for the result

  Returns:
    A dict with all the integers in the range [2, n) as keys where
    dict[p] is True iff p is prime.
  """
  primes = {}
  for i in xrange(2, n):
    if i in primes:
      continue
    primes[i] = True
    for j in xrange(2 * i, n, i):
      primes[j] = False
  return primes

def prime_factors(n):
  """Computes the prime factors of n
     This is a naive inefficient implementation.

  Args:
    n: the number to compute the prime factors for

  Return:
    A set with the prime factors of n
  """
  prime_factors = set()
  d = 1
  while n != 1:
    d += 1
    if n % d == 0:
      prime_factors.add(d)
      while n % d == 0:
        n /= d
  return prime_factors
