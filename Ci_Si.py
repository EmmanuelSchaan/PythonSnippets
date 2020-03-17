from pylab import *
from numpy import *
from scipy import special
 

# Ci(x) = - integrale( cos(t)/t, t=x..+infini)
# Si(x) = integrale( sin(t)/t, t=0..x)

X = linspace(.001, 100, 10001)
Si = special.sici(X)[0]
Ci = special.sici(X)[1]

figure(1)
hold(False)
plot(X, Ci, 'r-')
hold(True)
plot(X, Si, 'b-')


