import numpy as np
from scipy import integrate

a = -1.
b =  1.
f = lambda x: np.cos(x)*(1.+x)**0.4

# For comparison
quad, quad_err = integrate.quad(f, a, b, epsabs=0., epsrel=1.e-5)

# Gauss-Legendre (default interval is [-1, 1])
deg = 100
# computing the nodes and weights takes 2.5ms for deg=100
x, w = np.polynomial.legendre.leggauss(deg+1)
gauss = sum(w * f(x))

# Scipy's version of Gauss-Legendre, with fixed tolerance
gaussScipyFixedTol = integrate.quadrature(f, a, b, tol=0., rtol=1.e-5, maxiter=50, vec_func=False, miniter=1)

# Scipy's version of Gauss-Legendre, with fixed order
gaussScipyFixedOrder = integrate.fixed_quad(f, a, b, args=(), n=deg)


print 'Quad:', quad, quad_err
print 'Gauss-Legendre from numpy:', gauss
print 'Gauss-Legendre from scipy (fixed tol):', gaussScipyFixedTol
print 'Gauss-Legendre from scipy (fixed order):', gaussScipyFixedOrder
