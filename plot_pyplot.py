import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)


fig1 = plt.figure(1)
fig1.clf()
ax1 = fig1.add_axes([0.15, 0.1, 0.7, 0.3]) # [left, bottom, width, height]

line, = ax1.plot(t, s, color='blue', lw=2)

ax1.set_xlabel(r'$x$ axis')
ax1.set_ylabel(r'$y$ axis')