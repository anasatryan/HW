#Problem 1_HW3

import math

def main_function(x):
  return 1 / x - math.tan(x)

def bisection_method(func, bound_a, bound_b, stopping_condition):
  if func(bound_a) * func(bound_b) >= 0:
    print("Bisection method does not work for this case!")
    print((func(bound_a), func(bound_b)))
    return None

  midpoint = (bound_a + bound_b) / 2
  if abs(bound_a - bound_b) < stopping_condition:
    return midpoint

  midpoint_value = func(midpoint)
  upper_level = func(bound_b)
  lower_level = func(bound_a)
  
  if midpoint_value * lower_level < 0:
    return bisection_method (func, bound_a, midpoint, stopping_condition)
  elif midpoint_value * upper_level < 0:
    return bisection_method(func, midpoint,bound_b, stopping_condition)
  else:
    return (lower_level, midpoint_value, upper_level)

print (bisection_method (main_function, bound_a = 0.1, bound_b = math.pi / 2, stopping_condition = 10 ** (-4)))