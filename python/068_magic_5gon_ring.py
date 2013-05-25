from itertools import permutations
from operator import itemgetter

def is_solution(r):
  sums = [sum(w) for w in r]
  return all(sums[0] == i for i in sums)

def ring(r):
  return [[r[0], r[1], r[2]],
          [r[3], r[2], r[4]],
          [r[5], r[4], r[6]],
          [r[7], r[6], r[8]],
          [r[9], r[8], r[1]]]

def value(r):
  s = [l[0] for l in r]
  i, _ = min(enumerate([l[0] for l in r]), key=itemgetter(1))
  ret = []
  for k in xrange(5):
    ret.append(r[(i + k) % 5])
  return int("".join("".join([str(c) for c in l]) for l in ret))

result = 0
for permutation in permutations([1,2,3,4,5,6,7,8,9]):
  r = ring([10] + [i for i in permutation])
  if is_solution(r):
    result = max(result, value(r))
print result

