"""
For a rect of size NxM the number of contained rects is (N + 1choose 2)*(M + 1 choose 2).
That is, N*(N+1)*M*(M+1)/4.
"""
def f_rect(n, m):
  return n * (n + 1) * m * (m + 1) / 4

# arbitrary max rows to 4000
MAX = 4000
best_distance = float("inf")
best_area = 0
for n in xrange(1, MAX):
  for m in xrange(1, n + 1):
    distance = abs(2000000 - f_rect(n, m))
    if distance < best_distance:
      best_distance = distance
      best_area = m*n
print best_area

