#!/usr/bin/python
from itertools import product
from pygraph.classes.digraph import digraph
from pygraph.algorithms.minmax import shortest_path

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

DATA = load()
ROWS = len(DATA)
COLS = len(DATA[0])
NODES = []
for i in xrange(ROWS):
  row = []
  for j in xrange(COLS):
    row.append((i, j))
  NODES.append(row)
START = (-1, -1)
TARGET = NODES[ROWS - 1][COLS - 1]

def neighbours(node):
  i, j = node
  for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    if i + di < 0 or i + di >= ROWS or j + dj < 0 or j + dj >= COLS:
      continue
    yield NODES[i + di][j + dj]

gr = digraph()
gr.add_node(START)
for row in NODES:
  for node in row:
    gr.add_node(node)

for row in NODES:
  for node in row:
    for n in neighbours(node):
      gr.add_edge((node, n), wt=DATA[n[0]][n[1]])
gr.add_edge((START, NODES[0][0]), wt=DATA[0][0])
s, d = shortest_path(gr, START)
print d[TARGET]

