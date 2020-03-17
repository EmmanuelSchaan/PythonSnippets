# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from enthought.mayavi import mlab
import numpy as np
from scipy.special import sph_harm

# Create a sphere
r = 0.3
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0:pi:101j, 0:2*pi:101j]

x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)

mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 300))
mlab.clf()
# Represent spherical harmonics on the surface of the sphere
for l in range(0, 5):
    for m in range(l):
        s = sph_harm(m, l, theta, phi).real

        mlab.mesh(x+m, y-l, z, scalars=s, colormap='jet')

mlab.view(90, 70, 6.2, (-1.3, -2.9, 0.25))
mlab.show()