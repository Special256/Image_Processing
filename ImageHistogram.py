import sys
import numpy as np
import skimage.color
import skimage.io
from matplotlib import pyplot as plt

# grayscale histogram
image = skimage.io.imread(fname = sys.argv[1], as_gray = True)

skimage.io.imshow(image)

# create the histogram
def hist(img):
	histogram, bin_edges = np.histogram(img, bins = 256, range = (0,1))
	
	# draw the histogram
	plt.figure()
	plt.title("Grayscale Histogram")
	plt.xlabel("grayscale values")
	plt.ylabel("pixels")
	plt.xlim([0.0, 1.0])
	
	plt.plot(bin_edges[0:-1], histogram)
	plt.show()


hist(image)


# # colored histogram
# image2 = skimage.io.imread(fname = sys.argv[1])

# skimage.io.imshow(image2)


# # select RGB
# colors = ("red", "green", "blue")
# channel_ids = (0, 1, 2)

# # histogram for each color
# plt.figure()
# plt.title("Colored Histogram")
# plt.xlabel("Color Values")
# plt.ylabel("Pixels")
# plt.xlim([0, 256])
# for channel_id, c in zip(channel_ids, colors):
# 	histogram, bin_edges = np.histogram(image2[:, :, channel_id], bins = 256, range = (0, 256))
# 	plt.plot(bin_edges[0:-1], histogram, color = c)


# plt.show()
