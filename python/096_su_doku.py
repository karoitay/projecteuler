#!/usr/bin/python
from copy import deepcopy
from itertools import product

INPUT = "../inputs/sudoku.txt"
ZERO = ord("0")
ALL_CELLS = [cell for cell in product(xrange(9), repeat = 2)]
POSSIBILITIES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def to_string(val):
  if type(val) == int and val != 0:
    return str(val)
  if type(val) == set and len(val) == 1:
    return str(val.copy().pop())
  return "."

def print_grid(grid):
  sep = "-"*19
  print sep
  for i in xrange(9):
    print "|" + "".join([to_string(grid[i][j]) + {2:"|"}.get(j % 3, " ") for j in xrange(9)])
    if i % 3 == 2:
      print sep

def char_to_val(c):
  if c == "0":
    return set(POSSIBILITIES)
  return ord(c) - ZERO

def grids():
  with open(INPUT, 'r') as f:
    name = f.readline().strip()
    while  name != "":
      yield (name, [map(char_to_val, f.readline().strip()) for i in xrange(9)])
      name = f.readline().strip()

def is_solved(grid):
  return all(all(type(cell) == int for cell in row) for row in grid)

def row_of(row, cell, inclusive=False):
  return ((row, i) for i in xrange(9) if inclusive or i != cell)

def col_of(row, cell, inclusive=False):
  return ((i, cell) for i in xrange(9) if inclusive or i != row)

def block_of(row, cell, inclusive=False):
  r = 3 * (row / 3)
  c = 3 * (cell / 3)
  return ((r + i, c + j) for i, j in product(xrange(3), repeat=2)
          if inclusive or r + i != row or i + j != cell)

def update(grid, row, cell, val, debug):
  if (any(grid[r][c] == val for r, c in row_of(row, cell)) or
      any(grid[r][c] == val for r, c in col_of(row, cell)) or
      any(grid[r][c] == val for r, c in block_of(row, cell))):
    raise Exception
  grid[row][cell] = val
  if debug:
    print "Next update:", row, cell, val
    print_grid(grid)
    print
  return grid

def update_cell(grid, row, cell, val, debug):
  c_val = grid[row][cell]
  if type(c_val) == set and val in c_val:
    c_val.remove(val)
    if len(c_val) == 1:
      update(grid, row, cell, c_val.pop(), debug)
    return True
  return False

def update_cycle(grid, row, cell, debug):
  updated = False
  val = grid[row][cell]
  if type(val) != int:
    return updated
  for r, c in row_of(row, cell):
    updated = update_cell(grid, r, c, val, debug) or updated
  for r, c in col_of(row, cell):
    updated = update_cell(grid, r, c, val, debug) or updated
  for r, c in block_of(row, cell):
    updated = update_cell(grid, r, c, val, debug) or updated
  return updated

def try_harder_in_cells(grid, cells, val, debug):
  found = None
  for r, c in cells:
    if type(grid[r][c]) != set or not val in grid[r][c]:
      continue
    if found:
      return False
    found = (r, c)
  if not found:
    return False
  update(grid, found[0], found[1], val, debug)
  return True

def try_harder_in_row(grid, row, val, debug):
  return try_harder_in_cells(grid, row_of(row, 0, True), val, debug)

def try_harder_in_col(grid, col, val, debug):
  return try_harder_in_cells(grid, col_of(0, col, True), val, debug)

def try_harder_in_block(grid, block, val, debug):
  return try_harder_in_cells(grid, block_of(block / 3, 3 * (block % 3), True), val, debug)

def try_harder(grid, debug, val=0):
  return val == 0 and any(try_harder(grid, debug, i) for i in POSSIBILITIES) or any(
    try_harder_in_row(grid, i, val, debug) or
    try_harder_in_col(grid, i, val, debug) or
    try_harder_in_block(grid, i, val, debug) for i in xrange(9))

def progress(grid, debug):
  updated = False
  while (sum([update_cycle(grid, row, cell, debug) for row, cell in ALL_CELLS]) or
         try_harder(grid, debug)):
    updated = True
    continue
  return updated

def extend(grid, debug):
  m = min([len(grid[row][cell]) for row, cell in ALL_CELLS if type(grid[row][cell]) == set])
  for row, cell in ALL_CELLS:
    if type(grid[row][cell]) == set and len(grid[row][cell]) == m:
      for val in grid[row][cell]:
        yield update(deepcopy(grid), row, cell, val, debug)
      break

def solve(grid, debug=False):
  if debug:
    print_grid(grid)
  stack = [deepcopy(grid)]
  while len(stack) > 0:
    grid = stack.pop()
    try:
      progress(grid, debug)
    except Exception:
      continue # backtrack
    if is_solved(grid):
      return grid
    stack.extend(extend(grid, debug))
  return grid

s = 0
for name, grid in grids():
  print "Solving", name
  solved = solve(grid)
  if not is_solved(solved):
    solved = solve(grid, True)
    for r, c in ALL_CELLS:
      if type(solved[r][c]) == set:
        print r, c, solved[r][c]
    print_grid(solved)
    s = None
    break
  s += 100*solved[0][0] + 10*solved[0][1] + solved[0][2]
if s:
  print s
