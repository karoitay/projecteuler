#!/usr/bin/python
from utils.numbers import fibonacci_generator
print sum(f for f in fibonacci_generator(4000000) if f % 2 == 0)
