#!/usr/bin/python

from itertools import product
from math import sqrt

POINTS = range(51)
O = (0, 0)

def get_canonical_points(combination):
  x1, y1, x2, y2 = combination
  if x1 < x2 or x1 == x2 and y1 < y2:
    return (x1, y1), (x2, y2)
  else:
    return (x2, y2), (x1, y1)

def is_right_angle(triangle):
  P, Q = triangle
  if P == Q or P == O or Q == O:
    return False
  x1, y1 = P
  x2, y2 = Q

  PO = x1**2 + y1**2
  QO = x2**2 + y2**2
  PQ = (x2 - x1)**2 + (y2 - y1)**2
  
  T = sorted([PO, QO, PQ])
  return abs(T[0] + T[1] - T[2]) < 0.1

print sum(is_right_angle(triangle) for triangle in
  set(map(get_canonical_points, product(POINTS, repeat=4))))