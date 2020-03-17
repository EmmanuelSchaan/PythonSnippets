# Cette fonction permet de superposer a un graphe existant 
# des lignes paralleles, de pente slope
# X et Y sont les tableaux dej traces, de meme taille
# size est le rapport de l'etendue horizontale et verticale des
# lignes a celle du graphe Y = f(X)
# Nlines est le nombre de lignes (+_ 1...)
# offset est le decalage vertical des lignes en pourcentage de l'etendue
# verticale du graphe Y = f(X)

from pylab import *
from scipy import linspace


def DiagLines(X, Y, slope, size, Nlines, offset):
   N = len(X)

   xmin = X[0]
   xmax = X[0]
   xmean = X[0]
   for k in range (N):
      if X[k] < xmin:
         xmin = X[k]
      if X[k] > xmax:
         xmax = X[k]
   xmean = (xmin + xmax) / 2
   xmin = xmean - size * (xmean - xmin)
   xmax = xmean + size * (xmax - xmean)  

   ymin = Y[0]
   ymax = Y[0]
   ymean = Y[0]
   for k in range (N):
      if Y[k] < ymin:
         ymin = Y[k]
      if Y[k] > ymax:
         ymax = Y[k]
   ymean = (ymin + ymax) / 2
   ymin = ymean - size * (ymean - ymin)
   ymax = ymean + size * (ymax - ymean)  

   d = (ymax-ymin) + slope*(xmax-xmin)  # distance along y between the two extreme diagonal lines
   h = d / Nlines

   XX = linspace(xmin, xmax, int(N*size))
   XY = linspace(ymin, ymin + slope*(xmax-xmin), int(N*size))
   Y = zeros(( int(N*size), Nlines ))

   for k in range (Nlines):
      Y[:, k] = XY[:] + k * h - slope * (xmax-xmin) + (ymax-ymin) * offset/100
      plot(XX, Y[:, k], 'r--')

figure()
DiagLines(linspace(-10, 10, 100), linspace(-10, 10, 100), 5, 1., 10, 0.)