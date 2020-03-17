from pylab import *
from enthought.mayavi import mlab


I = 10 * rand(20, 30)



figure(3)
hold(False)
imshow(I)
xlabel(r'first argument of the array, inversed', fontsize=16)
ylabel(r'first argument of the array', fontsize=16)
hold(True)
axis('scaled') 
title(r'imshow', fontsize=20)
draw()   # or show() on some machines

mlab.figure(1)
mlab.surf(I)
mlab.axes()