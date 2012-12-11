
import copy

def compute(f):
  n = 1
  p = {}
  v = f(n)
  while v < 10000:
    if v > 999:
      s = str(v)
      s1,s2 = s[0:2], s[2:4]
      if not s1 in p:
        p[s1] = []
      p[s1].append(s2)
    n = n + 1
    v = f(n)
  return p

def dfs(polygonals, keys, chain=None, source=None, depth=None):
  result = []
  if chain == None or source == None or depth == None:
    depth = len(polygonals) - 1
    source = [None] + polygonals[1:]
    for k,values in polygonals[0].iteritems():
      for v in values:
        result = result + dfs(polygonals, keys, [(k,v)], source, depth)
    return result
  last = chain[-1][1]
  if depth == 0:
    if chain[0][0] == last:
      return [[int(s[0] + s[1]) for s in chain]]
    return []
  if not last in keys:
    return []
  for p in (i for i in keys[last] if source[i] != None):
    newsource = copy.copy(source)
    newsource[p] = None
    for v in polygonals[p][last]:
      newchain = copy.copy(chain)
      newchain.append((last,v))
      result = result + dfs(polygonals, keys, newchain, newsource, depth - 1)
  return result

polygonals = [
  (lambda n: n*(n+1)/2),
  (lambda n: n*n),
  (lambda n: n*(3*n-1)/2),
  (lambda n: n*(2*n-1)),
  (lambda n: n*(5*n-3)/2),
  (lambda n: n*(3*n-2)),
]
polygonals = [compute(f) for f in polygonals]
keys = {}
for i,p in enumerate(polygonals):
  for k in p.keys():
    if not k in keys:
      keys[k] = set()
    keys[k].add(i)
print [sum(l) for l in dfs(polygonals, keys)]