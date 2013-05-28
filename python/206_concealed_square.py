#!/usr/bin/python
"""
Need to find the only x so that (x^2 = 1_2_3_4_5_6_7_8_9_0 = y) where every _ is a single digit.
x must be greater than 10^9 and smaller than 10^10 because 10^9^2 = 10^18 < y and 10^10^2 = 10^20 > y.
Hence, x is a 10 digit number - sum(d_i*(10^i)) for i in 0..9.
We know that d_0^2 % 10 = 0 hence d_0 must be 0, which means y = 1_2_3_4_5_6_7_8_900
let x1 = x / 10
=> x^2 = x1^2*10^2 = y = y1*100
=> x1^2 = 1_2_3_4_5_6_7_8_9 = y1
=> x1 must end with either 3 or 7.
"""

MAX = 19293949596979899

def match(x):
  for i in xrange(9, 0, -1):
    if i != (x % 100) % 10:
      return False
    x = x / 100
  return True

def run():
  for i in xrange(10**7, 10**8):
    x_3 = i * 10 + 3
    x_7 = i * 10 + 7
    if match(x_3 ** 2):
      return x_3
    if match(x_7 ** 2):
      return x_7
    if x_7 ** 2 > MAX:
      print "Error", x_7
      return None

print run() * 10

