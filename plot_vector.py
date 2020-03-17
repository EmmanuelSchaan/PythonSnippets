import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(1)
ax=plt.subplot(111)
#
X = [0,0]   # x for tails of vectors
Y = [0,0]   # y for tails of vectors
U = [1, 2]  # Dx for vectors
V = [3,4]   # Dy for vectors
C = ['b', 'g']  # colors for the vectors
#
ax.quiver(X, Y, U, V, color=C,angles='xy',scale_units='xy',scale=1)

ax.set_xlim((-5., 5.))
ax.set_ylim((-5., 5.))



plt.show()