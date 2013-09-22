#!/usr/bin/python
from itertools import product
from collections import defaultdict

ROUNDS = 10**9

def compute_frequency(sides, dices):
  dist = defaultdict(int)
  for roll in product(xrange(1, sides + 1), repeat=dices):
    dist[sum(roll)] += 1
  total = float(sum(dist.values()))
  freq = {}
  for k, v in dist.iteritems():
    freq[k] = v/total
  return freq

peters = compute_frequency(4, 9)
colins = compute_frequency(6, 6)

peter_wins_probability = sum(freq * sum(colins[d] for d in xrange(6, roll))
  for roll, freq in peters.iteritems())
print round(peter_wins_probability, 7)
