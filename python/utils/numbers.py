def fibonacci_generator(stop=None):
  """Generator for Fibonacci series.
     Fibonacci series is defined recursively where f(n) = f(n-1) + f(n-2), f(0)=f(1)=1.

  Args:
    stop: An upper bound for the generation process.
          None means do not stop (the caller will be responsible for breaking the loop).
          Default is None
  Returns:
    A generator for Fibonacci series
  """

  if stop != None and stop < 2:
    return
  a, b = 1, 1
  yield a
  yield b
  next = a + b  
  while not stop or next < stop:
    yield next
    a, b = b, next
    next = a + b

def test_with_stop():
  from itertools import islice
  expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
  actual = [f for f in islice(fibonacci_generator(56), 10000)]
  assert expected == actual
  print "test_with_stop: PASS"

def test_without_stop():
  from itertools import islice
  expected = 354224848179261915075 # The 100th element
  actual = [f for f in islice(fibonacci_generator(), 100)][99]
  assert expected == actual
  print "test_without_stop: PASS"

def test():
  test_with_stop()
  test_without_stop()

if __name__ == "__main__":
  test()
