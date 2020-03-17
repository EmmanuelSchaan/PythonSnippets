import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter


##################################################################
# the random data
x = np.random.randn(1000)
y = np.random.randn(1000)


##################################################################
# definitions for the axes
left = bottom = 0.1
width = height = 0.65
extra = 0.2

scatter = [left, bottom, width, height]
histx = [left, bottom+height, width, extra]
histy = [left+width, bottom, extra, height]


##################################################################
# start with a rectangular Figure
plt.figure(1, figsize=(8,8))

axScatter = plt.axes(scatter)
axHistx = plt.axes(histx)
axHisty = plt.axes(histy)

# the scatter plot:
axScatter.plot(x, y, 'b+')

# now determine nice limits by hand:
xmin = -5.
xmax = 5.
ymin = -5.
ymax = 5.

axScatter.set_xlim( (xmin, xmax) )
axScatter.set_ylim( (ymin, ymax) )


##################################################################
# compute histogram for x
nbinsx = 21
binwidthx = (xmax-xmin)/(nbinsx-1)

Binsx = np.linspace(xmin, xmax, nbinsx)
Histx = np.histogram(x, Binsx)[0]

# plot histogram for x
axHistx.bar(Binsx[:-1], Histx, binwidthx, color='b')


##################################################################
# compute histogram for y
nbinsy = 31
binwidthy = (ymax-ymin)/(nbinsy-1)

Binsy = np.linspace(ymin, ymax, nbinsy)
Histy = np.histogram(y, Binsy)[0]

# plot histogram for y
axHisty.barh(Binsy[:-1], Histy, binwidthy, color='r')














