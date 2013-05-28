#!/usr/bin/python
import numpy

_MAX = 100

A = numpy.zeros((_MAX + 1, _MAX + 1), dtype=numpy.int)

def get_count(n, m):
  """How many options can we create n as
     as a sum of terms when all terms <= m"""
  if n == 1 or m == 1:
    return 1
  if m > n:
    return A[n][n]
  if n == m:
    return 1 + A[n][n - 1]

  return A[n - m][m] + A[n][m - 1]
  count = get_count(n - m, m) # for m + ...
  for i in xrange(1, m):
    # for the form i + ..., where i < m
    c = get_count(n - i, min(m, i))
    count = count + c
  return count

for i in xrange(1, _MAX + 1):
  for j in xrange(1, _MAX + 1):
    A[i][j] = get_count(i, j)
print A[_MAX][_MAX] - 1

