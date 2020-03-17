from pylab import *
from scipy import linspace


print('and this is the second subscript')

B = linspace(0, 1, 10)
savetxt('B.txt', B)