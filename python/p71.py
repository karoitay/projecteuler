MAX = 1000000

def arecoprime(a, b):
  while a != b:
    a_even = a % 2 == 0
    b_even = b % 2 == 0
    if a_even and b_even:
      return False
    elif a_even:
      a = a / 2
    elif b_even:
      b = b / 2
    elif a > b:
      a = (a - b) / 2
    else:
      b = (b - a) / 2
  return a == 1

max_num = 0
max_val = 0
max_denom = 0
for denom in xrange(3, MAX + 1):
  num = int((3 * denom - 1) / 7)
  if arecoprime(num, denom) and float(num) / denom > max_val:
    max_val = float(num) / denom
    max_num = num
    max_denom = denom
print max_num, "/", max_denom

