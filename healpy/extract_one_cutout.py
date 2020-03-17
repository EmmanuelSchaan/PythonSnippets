import healpy as hp
import numpy as np
import matplotlib.pyplot as plt

###########################################################################
# Extract one cutout map from a healpy map

# generate a random healpy map
nSide = 256
hMap = np.random.normal(size=hp.nside2npix(nSide))

# plot it
hp.mollview(hMap)
plt.show()


# map side in lon and lat
dLon = 10.# [deg]
dLat = 10.# [deg]
lonRange = (-dLon/2., dLon/2.) # [deg]
latRange = (-dLat/2., dLat/2.) # [deg]
pixRes = 0.5/60.  #0.5 / 60.  # [arcmin] to [deg]

# number of pixels on the side
xSize = np.int(np.ceil(dLon / pixRes))
ySize = np.int(np.ceil(dLat / pixRes))

# Check properties
print xSize, "pixel on the side,", dLon, "degrees on the side"
print "resolution is", dLon/xSize*60., "arcmin"

# position (lon, lat, psi) of the cutout center
lon = 45. # [deg]
lat = 45. # [deg]
pos = (lon, lat, 0.)

# extract the cutout
cutMap = hp.visufunc.cartview(hMap, rot=pos, lonra=lonRange, latra=latRange, xsize=xSize, ysize=ySize, return_projected_map=True, norm='hist')


# show it
plt.clf()
plt.imshow(cutMap.data)
plt.show()
