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
imageNumber = 2
# Set video dimension into height & width
height = 100
width = 100
result = np.zeros((height, width, 3))

currentImg = cv2.imread('video/0.jpg', cv2.IMREAD_COLOR)
for name in range(1,imageNumber):
	lastImg = currentImg
	currentImg = cv2.imread('video/'+str(name)+'.jpg', cv2.IMREAD_COLOR)

	for x in range(width):
		for y in range(height):
			if(currentImg[y, x].all() != lastImg[y, x].all()):
				result[y, x] += 1/imageNumber

# try:
#     rmtree('TEMP')
# except OSError:
#     print("Deletion of the directory failed")

print(result)

cv2.imshow('result.jpg', result)
cv2.imwrite('result.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
