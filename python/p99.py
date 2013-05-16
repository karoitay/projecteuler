from math import log

_FILE_NAME = "base_exp.txt"

def get_log(b, e):
  return e * log(b)

line_num = 0
max_line = 0
max_log = 0
with open(_FILE_NAME, "r") as f:
  for line in f:
    line_num = line_num + 1
    n = line.split(',')
    l = int(n[1]) * log(int(n[0]))
    if l > max_log:
      max_log = l
      max_line = line_num
print max_line
