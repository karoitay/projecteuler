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

data = load()
rows, cols = len(data), len(data[0])
result = [[None] * cols]
result[0][0] = data[0][0]
for i in xrange(1, rows):
  result.append([None] * cols)
  result[i][0] = data[i][0] + result[i - 1][0]
for i in xrange(1, cols):
  result[0][i] = result[0][i - 1] + data[0][i]
  for j in xrange(1, rows):
    result[j][i] = data[j][i] + min(result[j][i - 1], result[j - 1][i])
print result[rows - 1][cols - 1]

