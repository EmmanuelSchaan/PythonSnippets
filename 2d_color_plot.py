import matplotlib.pyplot as plt
import numpy as np


A = np.arange(12*10).reshape((12, 10))               


fig=plt.figure(0)
ax=plt.subplot(111)
#
imgplot = plt.imshow(A)
imgplot.set_interpolation('nearest')
imgplot.set_cmap('jet')
plt.colorbar()
#
ax.set_xlabel(r'y')
ax.set_ylabel(r'x')




plt.show()