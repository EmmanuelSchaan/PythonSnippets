#see help plot in python console

from pylab import *
from scipy import linspace


X = linspace(0, 2*pi, 100)
Y = zeros(100)
Y[:] = sin(X[:])
Z = cos(X)



figure(1)
hold(False)
plot(X, Y, 'r', linewidth = 1)   
axis('scaled')
grid()
xlabel(r'$abscisse$', fontsize=20) # the r before '  ' is only necessary if i want to insert latex characters like r'$\alpha$'
ylabel(r'$ordonnee$', fontsize=20)
hold(True)
title(r'$y=f(x)$', fontsize=20)

k = 1                               # saves the plot into a png file, with a given name
filename = 'test'+str(k)+'.png'
#savefig(filename)    
        
draw()




figure(2)
hold(False)
plot(X, Z, 'b--', linewidth = 2)  
xlabel(r'$abscisse$', fontsize=20)
ylabel(r'$ordonnee$', fontsize=20)
hold(True)
plot(X, Y, 'r:', linewidth = 3)
axis('scaled') 
grid()
title(r'$y=f(x)$', fontsize=20)
draw()





figure(3)
hold(False)

plot(X, Y, 'r', linewidth = 1) 
axis('scaled')
fig = figure(3)
axes = fig.get_axes()[0]
axes.set_xlim((0, 6))
axes.set_ylim((-0.5, 0.5))
grid()
xlabel(r'$abscisse$', fontsize=20)
ylabel(r'$ordonnee$', fontsize=20)
hold(True)
title(r'$y=f(x)$', fontsize=20)
draw()




figure(4)
hold(False)
loglog(X, Z, 'b--', linewidth = 2)          # log-log graph
axis('scaled') 
grid()
xlabel(r'$abscisse$', fontsize=20)
ylabel(r'$ordonnee$', fontsize=20)
hold(True)
title(r'$y=f(x)$, $loglog$', fontsize=20)
draw()




figure(5)
hold(False)
semilogx(X, Z, 'b,', linewidth = 2)          # semilogx or semilogy graph
axis('scaled') 
grid()
xlabel(r'$abscisse$', fontsize=20)
ylabel(r'$ordonnee$', fontsize=20)
hold(True)
title(r'$y=f(x)$, $semilogx$', fontsize=20)
draw()




figure(6)                                    # affiche une legende pour les courbes
hold(False)
p1, = plot(X, Y, 'b')
hold(True)
p2, = plot(X, Z, 'r')
hold(True)
p3, = plot(X, 2.*Z, 'g')

legend([p1, p3], [r'courbe numero 1', r'courbe numero 3'], loc=1)



import matplotlib.pyplot as plt              # barres d'erreur, pour loglog plot
XX = logspace(1., 3., 51)
YY = XX**(-4)
Yerr = 0.8*YY

plt.figure(7)
ax = plt.subplot(111)
ax.set_xscale("log", nonposx='clip')
ax.set_yscale("log", nonposy='clip')
plt.errorbar(XX, YY, yerr=Yerr, fmt='bo')
xlabel(r'$x$', fontsize=18)
ylabel(r'$e^{-x}$', fontsize=18)
title(r'error bars in loglog plot', fontsize=20)

