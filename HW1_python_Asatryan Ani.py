import math

for i in range (1,11):
   stirling_approximation = math.sqrt(2*math.pi*i)*(i/math.e)**i
   value = math.factorial(i)
   absolute_error = abs(value - stirling_approximation)
   relative_error = absolute_error / value
   print(f'n={i}, u={value}, v={stirling_approximation}, abserr(u,v)={absolute_error}, relerr(u,v)={relative_error}')