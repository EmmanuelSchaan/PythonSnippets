import numpy as np
import matplotlib.pyplot as plt
# to use flipper
import liteMap
# healpy
import healpy as hp
import pyfits

###################################################################

# fits file to be read
file_path = '/Users/Emmanuel/Desktop/kSZ/data/act_maps_14oct2014/deep5/cluster_mask.fits'


# print infos on the various HDUs (Header and Data Units)
print ""
print "Infos on the HDUs (Header and Data Units)"
pyfits.info(file_path)


###################################################################
# get infos about the header

# read header
header = pyfits.getheader(file_path)

print ""
print "Print the header keys"
print header.keys()

print ""
print "Value of the 'bitpix' card opject (2 ways)"
print header['bitpix']
print pyfits.getval(file_path, 'bitpix')

print ""
print "Use header card to see the comment associated with a keyword"
header_card = header.ascardlist()
print header_card['simple']


###################################################################
# get the data

# choose hdu to be read
hdu_number = 0 # 0 for the primary hdu
data = pyfits.getdata(file_path, hdu_number)
#data, header = pyfits.getdata(file_path, hdu_number, header=True)

print ""
print "Show the data type of the data"
print type(data)


print ""
print "Min and max values (it's a mask, so should be 0 and 1)"
print np.min(data)
print np.max(data)


