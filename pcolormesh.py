import numpy as np
import matplotlib.pyplot as plt


xMin = -10.
xMax = 10.
nX = 14  # nb of cells. nb of edges is nX+1
dX = (xMax-xMin)/nX
xCenters = np.linspace(xMin, xMax, nX)
xEdges = np.linspace(xMin-0.5*dX, xMax+0.5*dX, nX+1)

yMin = -3.
yMax = 3.
nY = 14
dY = (yMax-yMin)/nY
yCenters = np.linspace(yMin, yMax, nY)
yEdges = np.linspace(yMin-0.5*dY, yMax+0.5*dY, nY+1)


xx,yy = np.meshgrid(xEdges, yEdges, indexing='ij')
data = np.cos(xx)


fig=plt.figure(0)
ax=fig.add_subplot(111)
#
ax.pcolormesh(xx, yy, data, linewidth=0, rasterized=True, cmap=plt.cm.jet)
cp.set_clim(-1., 1.)
fig.colorbar(cp)
#
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')


plt.show()


