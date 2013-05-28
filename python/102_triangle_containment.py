#!/usr/bin/python
def area(A, B, C):
  return abs((A[0] - C[0]) * (B[1] - A[1]) - (A[0] - B[0]) * (C[1] - A[1])) / 2.

def solve_for_line(l):
  nums = [int(i) for i in l.strip().split(',')]
  A = (nums[0], nums[1])
  B = (nums[2], nums[3])
  C = (nums[4], nums[5])
  O = (0, 0)
  return area(A, B, C) == area(A, B, O) + area(A, C, O) + area(B, C, O)

with open("triangles.txt", "r") as f:
  print sum([solve_for_line(l) for l in f])

