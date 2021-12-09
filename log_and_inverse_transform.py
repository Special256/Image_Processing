# log transform
# Low inttensity values in the image are mapped to a wider range of output levels.
# the opposite is true for higher values
# s = R(r) = c*log(1+r)
# c = 255/(log(1+max_input_pixel_value))
# Application: Expands the dark pixels in the image while compressing the brighter pixels

import sys
import numpy as np
import skimage.color
import skimage.io
from matplotlib import pyplot as plt
from matplotlib.colors import NoNorm

# log transform
r = np.arange(0,256)
c = 255 / (np.log(1 + 255))
s = c * np.log (1 + r)

# inverse transform
y = np.exp(r ** 1 / c)- 1

plt.figure()
plt.plot(r, s)
plt.plot(r, y)
plt.show()

# read original image
image = skimage.io.imread(fname = sys.argv[1])
# image = skimage.io.imread("image_path")

# original image histogram
hist, bin_edges = np.histogram(image, bins = 256, range = (0, 256))

# apply log transform method
log_img = c * np.log (image + 1)

# convert float value to int
log_img = np.array(log_img, dtype = np.uint8)
# log imgae histogram
histogram, bin_edges = np.histogram(log_img, bins = 256, range = (0, 256))

# apply inverse transform method
inverse_image = np.exp(image ** 1 / c) - 1

# convert float value to int
inverse_image = np.array(inverse_image, dtype = np.uint8)
# inverse histogram
histo , bin_edges = np.histogram(inverse_image, bins = 256, range = (0, 256))

# plot histogram
plt.figure(figsize = (15, 4))
plt.subplot(1, 3, 1)
plt.xlim(0, 256)
plt.plot(bin_edges[0:-1], hist)
plt.subplot(1, 3, 1)
plt.xlim(0, 256)
plt.plot(bin_edges[0:-1], histogram)
plt.subplot(1, 3, 1)
plt.xlim(0, 256)
plt.plot(bin_edges[0:-1], histo)
plt.show()


# image plot
plt.figure(figsize = (15, 4))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap = 'gray', norm = NoNorm())
plt.subplot(1, 3, 2)
plt.imshow(log_img, cmap = 'gray', norm = NoNorm())
plt.subplot(1, 3, 3)
plt.imshow(inverse_image, cmap = 'gray', norm = NoNorm())
# plt.show()

# save images
plt.savefig('result.png')

def rgb_hist(img):

	# select RGB
	colors = ("red", "green", "blue")
	channel_ids = (0, 1, 2)
	
	# histogram for each color
	plt.figure()
	plt.title("Colored Histogram")
	plt.xlabel("Color Values")
	plt.ylabel("Pixels")
	plt.xlim([0, 256])
	for channel_id, c in zip(channel_ids, colors):
		histogram, bin_edges = np.histogram(img[:, :, channel_id], bins = 256, range = (0, 256))
		plt.plot(bin_edges[0:-1], histogram, color = c)
		
	plt.show()

rgb_hist(image)
rgb_hist(log_img)
rgb_hist(inverse_image)