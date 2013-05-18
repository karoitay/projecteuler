THRESHOLD = .99

def is_inc(n):
  m = 9
  while n != 0:
    d = n % 10
    if d > m:
      return False
    m = d
    n = n / 10
  return True

def is_dec(n):
  m = 0
  while n != 0:
    d = n % 10
    if d < m:
      return False
    m = d
    n = n / 10
  return True

def is_bouncy(n):
  return not (is_inc(n) or is_dec(n))

n = 100
bounces = 0.

while bounces/n < THRESHOLD:
  n += 1
  if is_bouncy(n):
    bounces += 1
print n
