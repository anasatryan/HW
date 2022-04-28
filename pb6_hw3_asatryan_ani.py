import math

def function(a):
  return lambda x: x ** 3 - a

def derivative_of_main(x):
  return (x ** 2) * 3

def Newton_method(main_function, derivative_of_function, initial_guess, epsilon, max_iteration = 1000):
  xn = initial_guess
  for n in range(0, max_iteration):
    function_value = main_function(xn)
    print(f"{n}-th iteration, Xn = {xn}, f(Xn) = {function_value}")
    if abs(function_value) < epsilon:
      print('Solution after', n, 'iterations.')
      return xn
    derivative_function_value = derivative_of_function(xn)
    if derivative_function_value == 0:
      print('zero derivative. No solution found.')
      return None
    xn = xn - function_value / derivative_function_value
  print('exceeded maximum number of iterations. No solution found.')
  return None


##when equal to 0, our initial guess is 0
print(Newton_method(function(0), derivative_of_main, 0, 0.00000001))

##when equal to 2, our initial guess is 1
print(Newton_method(function(2), derivative_of_main, 1, 0.00000001))

##when equal to 4, our initial guess is 1.5
##print(Newton_method(function(4), derivative_of_main, 1.5, 0.00000001))

##when equal to 10, our initial guess is 2
print(Newton_method(function(10), derivative_of_main, 2, 0.00000001))