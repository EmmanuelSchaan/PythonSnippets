import moby2
from matplotlib import pyplot as plt
import numpy as np


#filename = '/u/mhasse/WWW/public/secrets/maps_for_eschaan/deep5/patch_00_ar1.fits.gz'
#filename = '../../data/act_maps_14oct2014/deep5/patch_00_ar1.fits'
filename = '../../data/act_maps_14oct2014/deep6/patch_00_ar1.fits'


map0 = moby2.mapping.fits_map.spaceMap(filename)
map0.imshow(sigma=3)
plt.savefig('test.png')
plt.clf()
'''
# image data:
print map0.data.shape, map0.data.max()
# weight 

# coordsys:
#  "sky" ra,dec
#  "x,y" internal fits...
#  "i,j" ...
#  "J,I" pixel grid coordinates

# e.g. the pixel closest to ra,dec=(0,0)
I,J = map0.pixn.IJ_from_sky(0,0)
# Note transposition...
print map0.data[J,I]

# Help to extract stuff
map1 = map0.extract((1.,-1.),(1.,2.))
map1.imshow(sigma=3)
plt.savefig('test2.png')
plt.clf()

# Quick foray into Fourier plane
map1.data -= map1.data.mean()
fmap1 = map1.fftMap()
fmap1.imshow(data=abs(fmap1.data), units='ell')
plt.savefig('test3.png')
plt.clf()

ell = fmap1.radii() * 180/np.pi
filt = (ell > 1000)
fmap2 = fmap1.copy()
fmap2.data *= filt
map2 = fmap2.ifftMap()

map2.imshow(sigma=3)
plt.savefig('test4.png')
plt.clf()
'''
