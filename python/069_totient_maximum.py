#!/usr/bin/python
MAX = 1000000

def getdevisors():
  devisors = {}
  for i in xrange(2, MAX + 1):
    if i in devisors:
      continue
    for j in xrange(i, MAX + 1, i):
      devisors_j = devisors.get(j, [])
      devisors_j.append(i)
      devisors[j] = devisors_j
  return devisors

def getphi(n, devisors):
  devisors_n = devisors[n]
  phi = 1
  for p in devisors_n:
    k = 0
    while n % p == 0:
      k = k + 1
      n = n / p
    phi = phi * (p - 1) * (p ** (k - 1))
  return phi

devisors = getdevisors()
max_val = 0
max_arg = 0
for i in range(2, MAX + 1):
  val = i/float(getphi(i, devisors))
  if val > max_val:
    max_val = val
    max_arg = i
print "max arg=", max_arg, " val=", max_val

