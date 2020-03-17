from pylab import *
import numpy as np


# plot the confidence ellipse at percentage alpha
# for a 2d gaussian random vector (x,y),
# with mean (0,0)
# with std dev sx (resp. sy) for x (resp. y)
# and correlation coeff rho
def ConfidenceEllipse(rho, sx, sy, alpha, colorstring, fignb):
   
   R = np.sqrt( -2.*np.log(1.-alpha) )
   
   Y = np.linspace(-sy*R, sy*R, 101)
   X1 = rho*sx*Y/sy + np.sqrt( (1.-rho**2) * (sx**2 * R**2 - (sx*Y/sy)**2) )
   X2 = rho*sx*Y/sy - np.sqrt( (1.-rho**2) * (sx**2 * R**2 - (sx*Y/sy)**2) )
   
   figure(fignb)
   plot(X1, Y, colorstring)
   hold(True)
   plot(X2, Y, colorstring)
   hold(True)



ConfidenceEllipse(0.99, 2., 3., 0.68, 'b--', 0)