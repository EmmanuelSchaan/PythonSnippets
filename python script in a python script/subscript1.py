from pylab import *
from scipy import linspace


print('this is the first subscript')

A = linspace(0, 1, 10)
savetxt('A.txt', A)