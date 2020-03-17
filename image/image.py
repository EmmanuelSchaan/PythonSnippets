import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# read the image
img=mpimg.imread('stinkbug.png')

# show the image
plt.figure(1)
imgplot = plt.imshow(img)

# do a slicing to keep only one of the three R,G,B colors
lum_img = img[:,:,0]

# show the result
plt.figure(2)
plt.clf()
imgplot = plt.imshow(lum_img)

# choose the color code
imgplot.set_cmap('jet')
#imgplot.set_cmap('hot')
#imgplot.set_cmap('spectral')

# display the color bar
plt.colorbar()

# rescale the color code to be from 0.1 to 0.7 instead of 0. and 1.
imgplot.set_clim(0.1,0.7)



# resizing the image
import Image
img = Image.open('stinkbug.png')    # Open image as PIL image object
rsize = img.resize((img.size[0]*2.,img.size[1]/2.)) # Use PIL to resize
rsizeArr = np.asarray(rsize)  # Get array back
plt.figure(4)
imgplot = plt.imshow(rsizeArr)   # show the result




