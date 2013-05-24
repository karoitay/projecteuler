def getprimes(n):
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

