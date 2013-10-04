#!/usr/bin/python
from collections import defaultdict
MAX = 1000000

def generate_devisors_sums():
  devisors_sums = defaultdict(lambda: 1)
  for d in xrange(2, MAX):
    for n in xrange(2*d, MAX, d):
      devisors_sums[n] += d
  return devisors_sums

def get_chain(devisors_sums, n):
  chain = set()
  current = n
  while not current in chain and current < MAX and current > 1:
    chain.add(current)
    current = devisors_sums[current]
  if current == n:
    return chain
  return None

devisors_sums = generate_devisors_sums()
chains = {}
for n in xrange(MAX):
  if n in chains:
    continue
  chain = get_chain(devisors_sums, n)
  if not chain:
    continue
  l, m = len(chain), min(chain)
  for c in chain:
    chains[c] = (l, m)
print max(chains.values())[1]
