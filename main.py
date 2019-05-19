import numpy as np
import cv2
import os
from shutil import rmtree

video = cv2.VideoCapture('video/crowd.mp4')
success,image = video.read()

## Global informations on the video
fps = int(video.get(5))
imageNumber = int(video.get(7)) + 1
height = int(video.get(4))
width = int(video.get(3))
print('fps:', fps, '| number of images:', imageNumber, '| height:', height, '| width:', width)

## Time informations
jumpImg = 500
video.set(cv2.CAP_PROP_POS_AVI_RATIO,1)
duration = video.get(cv2.CAP_PROP_POS_MSEC)
video.set(cv2.CAP_PROP_POS_AVI_RATIO,0)
repeating = int(duration/jumpImg)
print('duration:', duration, '| picking an image every:', jumpImg, '| number of picken image:', repeating)

result = np.zeros((height, width, 3))

success, lastImg = video.read()
time = jumpImg
video.set(cv2.CAP_PROP_POS_MSEC, time)
success, currentImg = video.read()
while success:
	for x in range(width):
		for y in range(height):
			if np.any(np.absolute(currentImg[y, x] - lastImg[y, x]) >= 250):
				result[y, x] += 255 / repeating
	lastImg = currentImg
	print(int(time/jumpImg), '/', repeating, '-', int(time/jumpImg/repeating*100), '%')
	time += jumpImg
	video.set(cv2.CAP_PROP_POS_MSEC, time)
	success, currentImg = video.read()

cv2.imshow('result.jpg', result/255)
cv2.imwrite('result.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
