#!/usr/bin/python
import math 

def compute(n):
  p, s = n, 0
  while int(math.log(p, 10)) == s: s, p = s + 1, p * n
  return s

print sum([compute(i) for i in range(1, 10)])