#!/usr/bin/python

MAX = 10**8

def get_squares_sums():
  from math import sqrt, ceil
  m = int(ceil(sqrt(MAX)))
  squares_sums = [0]*m
  for i in xrange(1, m):
    squares_sums[i] = squares_sums[i-1] + i*i
  return squares_sums

def is_palindrom(n):
  s = str(n)
  return s == s[::-1]

squares_sums = get_squares_sums()
unique = set()
l = len(squares_sums)
for lower in xrange(1, l):
  up_to_lower = squares_sums[lower - 1]
  for upper in xrange(lower + 1, l):
    squares_sum = squares_sums[upper] - up_to_lower
    if squares_sum >= MAX:
      break
    if is_palindrom(squares_sum):
      unique.add(squares_sum)

print sum(unique)
