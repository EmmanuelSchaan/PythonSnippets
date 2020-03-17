import healpy as hp
import numpy as np
import matplotlib.pyplot as plt


###########################################################################
# Plot a polygon on a healpy map
# here one octant of the sky

# version with theta, phi [rad]
theta = [0., np.pi/2., np.pi/2.]
phi = [0., 0., np.pi/2.]
xyz = hp.ang2vec(theta, phi)

nSide = 256
hMap = np.zeros(hp.nside2npix(nSide))
I = hp.query_polygon(nSide, xyz)
hMap[I] += 1.
hp.mollview(hMap)
plt.show()


# version with lon, lat [deg]
lat = [90., 0., 0.]
lon = [0., 0., 90.]
xyz = hp.ang2vec(lon, lat, lonlat=True)

nSide = 256
hMap = np.zeros(hp.nside2npix(nSide))
I = hp.query_polygon(nSide, xyz)
hMap[I] += 1.
hp.mollview(hMap)
plt.show()
