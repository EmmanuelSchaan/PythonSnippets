from pylab import *
from numpy import *
from scipy.interpolate import RectBivariateSpline

##################################################################################
# initial array of x and y
Xold = linspace(0., 1., 31) 
Yold = linspace(-1., 1., 31)

YYold, XXold = meshgrid(Yold, Xold)

# initial array of f(x,y)
OldFunction = cos(2*pi*XXold) * sin(2*pi*YYold)

##################################################################################
# new array of x and y
Xnew = linspace(0., 1., 101)
Ynew = linspace(-1., 1., 101)

YYnew, XXnew = meshgrid(Ynew, Xnew)

##################################################################################
# interpolation from initial arrays 
fFunction = RectBivariateSpline(Xold, Yold, OldFunction, s=0)

# creation of interpolated array
NewFunction = fFunction(Xnew, Ynew)

##################################################################################
# 2D plots to visually check the interpolation

print("plot old array")
figure(0)
hold(False)
pcolor(XXold, YYold, OldFunction)
colorbar()
title('Initial, sparsely sampled version')
draw()

print("plot new array")
figure(1)
hold(False)
pcolor(XXnew, YYnew, NewFunction)
colorbar()
title('Reconstructed, finely sampled version')
draw()

##################################################################################
# comparing slices at fixed y for the initial and reconstructed arrays

print("compare curves")
figure(2)
hold(False)

for i in range( len(Yold) ):
      plot(Xold, OldFunction[:, i], '-')
      hold(True)

for i in range( len(Ynew) ):
      plot(Xnew, NewFunction[:, i], '--')
      hold(True)









