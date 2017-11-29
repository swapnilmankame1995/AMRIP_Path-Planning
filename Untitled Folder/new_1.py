import cv2
import numpy as np
import imutils


img = cv2.imread('cp1.png')
blur = cv2.GaussianBlur(img, (15, 15), 2)
#hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lower_range = np.array([100, 120, 125])
upper_range = np.array([155, 150, 140])

mask = cv2.inRange(hsv, lower_range, upper_range)
masked_img = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('image', img)
cv2.imshow('', masked_img)
cv2.imshow('Gaussian Blurring',blur)

while(True):
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2.destroyAllWindows()