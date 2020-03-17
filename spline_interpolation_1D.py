from pylab import *
from numpy import *
from scipy import *
from scipy.interpolate import interp1d, UnivariateSpline







NX = 51

X = 2*pi* sqrt( linspace(0.0, 1.0, NX) )
Y = cos(X)
Xlin = 2*pi*linspace(0.0, 1.0, NX)


# two interpolation modules from scipy.special
i = interp1d(X,Y,kind='linear')
u = UnivariateSpline(X,Y,k=3,s=0)

# numpy.interp gives directly an array with the linear interpolation
# Attention: X has to be sorted in growing order
Ylin = interp(Xlin, X, Y)



figure(1)
hold(False)
plot(X, Y,'r,')
hold(True)
plot(Xlin, i(Xlin),'b--')
hold(True)
plot(Xlin, u(Xlin),'g--')
hold(True)
plot(Xlin, Ylin,'k--')
draw()











