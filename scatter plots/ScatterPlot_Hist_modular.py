import numpy as np
import matplotlib.pyplot as plt

##################################################################
# the random data
x = np.random.randn(1000)
y = np.random.randn(1000)


##################################################################
def ScatterPlot(x, y, rho, sx, sy, alpha, fignb):
   # create figure
   plt.figure(fignb, figsize=(8,8))
   
   # definitions for the axes
   left = bottom = 0.1
   width = height = 0.65
   scatter = [left, bottom, width, height]
   axScatter = plt.axes(scatter)

   # the scatter plot:
   axScatter.plot(x, y, 'b+')
   
   # draw ellipse at 68% confidence
   R = np.sqrt( -2.*np.log(1.-alpha) )
   
   Y = np.linspace(-sy*R, sy*R, 101)
   X1 = rho*sx*Y/sy + np.sqrt( (1.-rho**2) * (sx**2 * R**2 - (sx*Y/sy)**2) )
   X2 = rho*sx*Y/sy - np.sqrt( (1.-rho**2) * (sx**2 * R**2 - (sx*Y/sy)**2) )
   
   axScatter.plot(X1, Y, 'r--')
   axScatter.plot(X2, Y, 'r--')
   
   
##################################################################
def Histogram(x, xmin, xmax, nbins, sx, fignb, horiz_verti):
   # compute histogram for x
   left = bottom = 0.1
   width = height = 0.65
   extra = 0.2
   
   # define position of figure
   if horiz_verti == "horizontal":
      hist = [left, bottom+height, width, extra]
   elif horiz_verti == "vertical":
      hist = [left+width, bottom, extra, height]
   
   # create figure
   axHist = plt.axes(hist)
   
   # compute histogram
   binwidth = (xmax-xmin)/(nbins-1)
   Bins = np.linspace(xmin, xmax, nbins)
   Hist = np.histogram(x, Bins)[0]

   # plot histogram, vertical or horizontal
   if horiz_verti == "horizontal":
      axHist.bar(Bins[:-1], Hist, binwidth, color='b', alpha = 0.3)
   elif horiz_verti == "vertical":
      axHist.barh(Bins[:-1], Hist, binwidth, color='b', alpha = 0.3)



##################################################################
# call the functions
ScatterPlot(x, y, 0.8, 1., 2., 0.68, 0)
Histogram(x, -5., 5., 21, 3., 0, "horizontal")
Histogram(y, -5., 5., 21, 3., 0, "vertical")










