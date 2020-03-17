# gives the correctly normalized fourier transform
# also shows the effect of aliasing, when the sampling is too small

import numpy as np
import matplotlib.pyplot as plt


# time
tmin = -10.
tmax = 10.
Nt = 22
Dt = (tmax-tmin)
dt = Dt / (Nt-1.)
T = np.linspace(tmin, tmax, Nt)

# pulsations (omega = 2pi frequency)
omegaf = 2.*np.pi/Dt # fundamental pulsation
Omega = np.array([i * omegaf for i in range(Nt//2 + 1)])
Freq = Omega / (2.*np.pi)


# input function
omega0 = 0.5
X = np.exp(-0.5*T**2 / omega0**2)
X /= np.sqrt(2.*np.pi*omega0**2)

# Fourier transform
Y = np.fft.rfft(X)   # fft for real signal X
Y *= dt



print "min freq:", Freq[1]
print "max freq:", Freq[-1]

# expected fourier transform
Ytheory = np.exp(-0.5 * omega0**2 * Omega**2)
Yaliased = Ytheory + np.exp(-0.5 * omega0**2 * (Omega[-1] + Omega[::-1])**2)

# plot the function
fig=plt.figure(0)
ax=fig.add_subplot(111)
#
ax.plot(T, X)
#
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$f(t)$')

# plot the power spectrum
fig=plt.figure(1)
ax=fig.add_subplot(111)
#
ax.plot(Omega, np.abs(Y)**2, 'b')
ax.plot(Omega, Ytheory**2, 'r--')
ax.plot(Omega, Yaliased**2, 'g--')
#
ax.set_xlabel(r'$\omega$')
ax.set_ylabel(r'$| \tilde{f}(\omega) |^2$')

plt.show()


