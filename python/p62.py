import math
import itertools

MAX_LEN = 10
LEN = 5

def key(n):
  l = [0]*10
  while n != 0:
    i = n % 10
    n = n / 10
    l[i] = l[i] + 1
  return "".join((str(d) for d in l))

def search(n):
  d = {}
  cube = n**3
  current_len = int(math.log(cube, 10))
  while current_len == int(math.log(cube, 10)):
    k = key(cube)
    if not k in d:
      d[k] = []
    d[k].append(cube)
    n = n + 1
    cube = n**3
  l = [v for v in d.values() if len(v) == LEN]
  if len(l) == 0:
    return n
  else:
    return l

n = 1
while type(n) == int:
  n = search(n)
print min([v[0] for v in n])