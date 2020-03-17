###########################################################################
# extract set of non-overlapping square cutouts from an octant of the sky (for Sehgal maps)

import healpy as hp
import numpy as np
import matplotlib.pyplot as plt


# cutout dimensions
# map side in lon and lat
dLon = 10.# [deg]
dLat = 10.# [deg]
lonRange = (-dLon/2., dLon/2.) # [deg]
latRange = (-dLat/2., dLat/2.) # [deg]
pixRes = 0.5/60.  #0.5 / 60.  # [arcmin] to [deg]
# number of pixels on the side
xSize = np.int(np.ceil(dLon / pixRes))
ySize = np.int(np.ceil(dLat / pixRes))


# create an empty map, to check footprints
nSide = 256
hMap = np.zeros(hp.nside2npix(nSide))


# offsets in lon and lat to start the cutouts
latStart = 0.
lonStart = 0.
# space between cutouts, to avoid overlap
space = 0.5 # [deg]


# latitudes of centers of cutouts
nPatches = 0
LatCenter = np.arange(latStart + dLat/2., 90., dLat + space)
for latCenter in LatCenter:
   latUpper = latCenter + dLat/2.
   latLower = latCenter - dLat/2.
   
   dLonCenter = dLon / np.cos(latCenter * np.pi/180.)
   dLonUpper = dLon / np.cos(latUpper * np.pi/180.)
   dLonLower = dLon / np.cos(latLower * np.pi/180.)
   LonCenter = np.arange(lonStart + dLonUpper/2., 90., dLonUpper + space)
   
   for lonCenter in LonCenter:
      
      # polygon edges
      latEdges = np.array([latUpper, latLower, latLower, latUpper])
      lonEdges = np.array([lonCenter-dLonUpper/2., lonCenter-dLonLower/2., lonCenter+dLonLower/2., lonCenter+dLonUpper/2.])
      
      # check that the cutout is entirely within the quadrant
      patchFits = np.sum(latEdges<0.) + np.sum(latEdges>90.) + np.sum(lonEdges<0.) + np.sum(lonEdges>90.)
      patchFits = patchFits==0.
      
      # if it fits
      if patchFits:
         nPatches += 1
         # plot the footprint
         xyz = hp.ang2vec(lonEdges, latEdges, lonlat=True)
         I = hp.query_polygon(nSide, xyz)
         hMap[I] += 1.
         
         # extract the cutout
         #pos = (lonCenter, latCenter, 0.)
         #cutMap = hp.visufunc.cartview(hMap, rot=pos, lonra=lonRange, latra=latRange, xsize=xSize, ysize=ySize, return_projected_map=True, norm='hist')
         
         # plot the cutout
         #plt.clf()
         #plt.imshow(cutMap)
         #plt.show()
         
print "Extracted "+str(nPatches)+" cutouts"

hp.mollview(hMap)
plt.show()

      




