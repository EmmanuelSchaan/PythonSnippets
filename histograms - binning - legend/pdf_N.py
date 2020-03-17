import numpy as np
from pylab import *
from scipy.integrate import quad

nfiles = 1000

# nb of halos found in each of the nfiles realizations
Nhalos = genfromtxt("Nhalos.txt")
Nav = np.average(Nhalos)


# Building histogram
nbins = 51
firstbin = 0.
lastbin = 300.
binwidth = (lastbin-firstbin)/(nbins-1)

Bins = linspace(firstbin, lastbin, nbins)
NhalosHist = np.histogram(Nhalos, Bins)[0]


# gaussian approximation to the Poisson PDF
fPDF = lambda n: (2*pi*Nav)**(-1./2.) * exp(- (n - Nav)**2 / (2*Nav))

# expected histogram from the PDF
g = lambda i: quad(fPDF, Bins[i], Bins[i+1], epsabs = 0, epsrel = 1.e-3)[0]
ExpectedHist = nfiles * np.array(map( g, linspace(0, nbins-2, nbins-1) ))




figure(2)
hold(False)
# plotting the histogram with bars
bar1 = bar(Bins[:-1], NhalosHist, binwidth, color='b', label='from simulation')
hold(True)
# plotting the histogram with bars
bar2 = bar(Bins[:-1], ExpectedHist, binwidth, color='r', alpha = 0.5, label='gaussian pdf')
hold(True)
axes = figure(2).get_axes()[0]
axes.set_xlim((firstbin, lastbin))
xlabel(r'$N_{M > M_{cutoff}}$', fontsize=18)
title(r'PDF of $N_{M > M_{cutoff}}$', fontsize=20)
legend((bar1[0], bar2[0]), ('from simulation', 'gaussian pdf'), loc=2)

