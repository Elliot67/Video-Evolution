# To dectect exact pixels modification use: if not(np.any(np.absolute(currentImg[y, x] - lastImg[y, x]) == 0)):

import numpy as np
import cv2
import os
from shutil import rmtree

# try:
#     os.mkdir('TEMP')
# except OSError:
#     print("Creation of the temporary directory failed. (The TEMP folder may already exist. Delete or rename it, and try again.)")
#

# Transform video to sequence of image
# Change the number of frame between each image

# Set number of Image in the TEMP folder
imageNumber = 29
# Set video dimension into height & width
height = 360
width = 640
result = np.zeros((height, width, 3))

lastImg = cv2.imread('video/TEMP/number0.tif', cv2.IMREAD_COLOR)
for name in range(1,imageNumber):
	currentImg = cv2.imread('video/TEMP/number'+str(name)+'.tif', cv2.IMREAD_COLOR)
	print(name)

	for x in range(width):
		for y in range(height):
			if np.any(np.absolute(currentImg[y, x] - lastImg[y, x]) >= 20):
				result[y, x] += 255/(imageNumber - 1)
	lastImg = currentImg


# try:
#     rmtree('TEMP')
# except OSError:
#     print("Deletion of the directory failed")

cv2.imshow('result.tif', result/255)
cv2.imwrite('result.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
