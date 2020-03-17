from pylab import *
from numpy import *
from enthought.mayavi import mlab
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



thetai = (pi/180) * 0.
thetaf = (pi/180) * 180.
Ntheta = 40

phii = (pi/180) * 0.
phif = (pi/180) * 360.
Nphi = 60

THETA = linspace(thetai, thetaf, Ntheta)
PHI = linspace(phii, phif, Nphi)


RADIUS = ones((Ntheta, Nphi))           # this is the radius function
for i in range (Ntheta):
   for j in range (Nphi):
      RADIUS[i, j] = cos( THETA[i] + PHI[j] )

################################################################

xx = zeros((Ntheta, Nphi))
yy = zeros((Ntheta, Nphi))
zz = zeros((Ntheta, Nphi))

for i in range (Ntheta):
   for j in range (Nphi):
      xx[i, j] = sin(THETA[i]) * cos(PHI[j])
      yy[i, j] = sin(THETA[i]) * sin(PHI[j])
      zz[i, j] = cos(THETA[i])


############################### MAYAVI #################################

mlab.figure('Radius')
mlab.mesh(xx, yy, zz, scalars=RADIUS, colormap='jet')
mlab.colorbar()
mlab.draw()

mlab.figure('Radius (bis)')
mlab.mesh(RADIUS*xx, RADIUS*yy, RADIUS*zz, colormap='jet')
mlab.colorbar()
mlab.draw()


############################## PYPLOT ##################################

xx = RADIUS * xx
yy = RADIUS * yy
zz = RADIUS * zz

figure(0)
fig = plt.figure(0)
ax = Axes3D(fig)
ax.scatter3D(ravel(xx),ravel(yy),ravel(zz))
plt.draw()


figure(10)
fig = plt.figure(10)
ax = Axes3D(fig)
ax.plot_wireframe(xx, yy, zz)
plt.draw()

figure(11)
fig = plt.figure(11)
ax = Axes3D(fig)
ax.plot_wireframe(xx, yy, zz)
ax.plot_surface(xx, yy, zz)
plt.draw()
