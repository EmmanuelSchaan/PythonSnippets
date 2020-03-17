import numpy as np
import matplotlib.pyplot as plt
# to use flipper
import liteMap
# healpy
import healpy as hp
import pyfits

###################################################################

# fits file to be read
#file_path = '/Users/Emmanuel/Desktop/kSZ/data/CMASS_DR10/mask_DR10v8_CMASS_North.fits'
file_path = '/Users/Emmanuel/Desktop/kSZ/data/CMASS_DR10/galaxy_DR10v8_CMASS_North-specObj.fits'


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
print "Properties of 10 first objects"
for iobj in range(10):
   print 'ra', data[iobj]['plug_ra'], ', dec', data[iobj]['plug_dec'], ', z', data[iobj]['z']


print ""
print "min redshift"
print np.min(data[:]['z'])
print "mean redshift"
print np.mean(data[:]['z'])
print "max redshift"
print np.max(data[:]['z'])



