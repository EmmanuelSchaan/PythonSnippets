from pylab import *
from enthought.mayavi import mlab

xi = 1.
xf = 2.
Nx = 10

yi = 3.
yf = 4.
Ny = 30


I = floor( 10*rand(Nx, Ny) )

xx = zeros((Nx+1,Ny+1))               # the dimension has to be one greater than for I, for pcolor
yy = zeros((Nx+1,Ny+1))
for i in range (Nx+1):
   yy[i,:] = linspace(yi, yf, Ny+1)
for j in range (Ny+1):
   xx[:,j] = linspace(xi, xf, Nx+1)



figure(1)
hold(False)
pcolor(xx, yy, I)
colorbar()
xlabel(r'$x$', fontsize=16)
ylabel(r'$y$', fontsize=16)
hold(True)
axis('scaled') 
title(r'pcolor', fontsize=20)
draw()
