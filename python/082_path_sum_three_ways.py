#!/usr/bin/python
def loadexample():
  return [[131, 673, 234, 103, 18 ],
          [201, 96 , 342, 965, 150],
          [630, 803, 746, 422, 111],
          [537, 699, 497, 121, 956],
          [805, 732, 524, 37 , 331]]

def load():
  data = []
  with open("matrix.txt", "r") as f:
    for line in f:
      data.append([int(n) for n in line.strip().split(',')])
  return data

def compute(data, result, i, j, k):
  """ Gets the value of getting to data[i][j] if we enter the j'th
      column from the k'th row"""
  value = result[k][j - 1]
  start = min(i, k)
  end = max(i, k) + 1
  for p in xrange(start, end):
    value += data[p][j]
  return value

data = load()
rows, cols = len(data), len(data[0])
result = []
for i in xrange(rows):
  result.append([None] * cols)
  result[i][0] = data[i][0]
for i in xrange(1, cols):
  for j in xrange(rows):
    result[j][i] = min([compute(data, result, j, i, k) for k in xrange(rows)])
print min([row[cols - 1] for row in result])

