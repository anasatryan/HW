import math

def f(x):
  return x - math.log10 (x) - 1000 ** 0.25 + 0.75

def g(x):
  return math.log10 (x) + 1000 ** 0.25 - 0.75

x0 = 1
x1 = g(x0)

while abs(x0 - x1) >= 10 ** (-4):
  x0 = x1
  x1 = g(x0)

print(x1)