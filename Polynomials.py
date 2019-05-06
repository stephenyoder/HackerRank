import numpy

polynomial = input()
x = input()
polynomial = polynomial.split()
print(polynomial)
print('\n')
print(numpy.polyval(polynomial, x))   #Output : 34
#numpy.polyval([1, -2, 0, 2], 4)   #Output : 34