from pylab import *
from numpy import *


my_array = floor( 10*rand(4, 5) )
print(my_array)

savetxt("myfile.txt", my_array)

recovered_array = genfromtxt("myfile.txt")
print(recovered_array)