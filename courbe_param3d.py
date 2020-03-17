from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


x = [6, 3, 6, 9, 12, 24]
y = [3, 5, 78, 12, 23, 56]
z = [10, 10, 10, 4, 5, 6]


figure(11)
fig = plt.figure(11)
ax = Axes3D(fig)
ax.plot(x, y, z)
plt.draw()
