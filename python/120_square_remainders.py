#!/usr/bin/python

# Computes the value of ((a - 1)^n + (a + 1)^n) % a^2 when a,n are integers, n>=0 and a>=3.
# By writing (a - 1)^n and (a + 1)^n in the binomial coefficient form
# and add them modulo a^2, all the terms the degree >= 2 are cancelled
# and we will get that:
# r(a, n) = 2 if n is even and (2an % a^2) if n is odd.
# Also note that if n >= 2a we will get r(a, n) == r(a, n % 2a).
def r(a, n):
  #assert type(a) == int, "a must be an int, provided: %s (%s)" % (a, type(a))
  #assert type(n) == int, "n must be an int, provided: %s (%s)" % (n, type(n))
  #assert a >= 3, "a must be >= 3, provided: %s" % a
  #assert n >= 0, "a must be >= 0, provided: %s" % n
  if n % 2 == 0:
    return 2
  return (2*(n % (2*a))*a) % (a**2)

# Computes max(r(a, n)) when a,n are integers, n>=0 and a>=3.
# Note that since for n>=2a we get r(a, n) == r(a, n % 2a) we only need to compute
# r(a,n) for 0 <= n < 2a.
def r_max(a):
  #assert type(a) == int, "a must be an int, provided: %s (%s)" % (a, type(a))
  #assert a >= 3, "a must be >= 3, provided: %s" % a
  return max(r(a, n) for n in xrange(2*a))

print sum(r_max(a) for a in xrange(3, 1001))
