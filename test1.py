import cv2
import numpy as np
from matplotlib import pyplot as plt
#import imutils


img = cv2.imread('cp1.png')


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5), np.uint8)

lower_range = np.array([115, 118, 118])
upper_range = np.array([150, 170, 170])

mask = cv2.inRange(hsv, lower_range, upper_range)
img_dilate = cv2.dilate(mask, kernel, iterations=2)
ret,thresh3 = cv2.threshold(img_dilate,65,255,cv2.THRESH_TRUNC)
ret,thresh1 = cv2.threshold(img_dilate,110,255,cv2.THRESH_BINARY_INV)

#img_erosion = cv2.erode(img_dilate, kernel, iterations=1)
#process_img =cv2.medianBlur(img_erosion,5)
#smoothed = cv2.filter2D(mask,-1,kernel)
#blur = cv2.GaussianBlur(img_dilate,(15,15),0)
#bilateral = cv2.bilateralFilter(mask,15,75,75)

# ------------------Image show part-------------

#cv2.imshow('image', img)
#cv2.imshow('erosion', img_erosion)
#cv2.imshow('smooth',smoothed)
#cv2.imshow('Gaussian Blurring',blur)
#cv2.imshow('bilateral Blur',bilateral)
#cv2.imshow('noiseless',process_img)
#cv2.imshow('op', thresh3)

# cv2.imshow('dailation', img_dilate)
# cv2.imshow('mask', mask)

# ------------------Image show part-------------

#res = cv2.bitwise_and(frame,frame, mask= mask)
image =[img_dilate,thresh3,thresh1]

#---------------Rescaling of image-----------

resized_image = cv2.resize(img_dilate,(2222,2229))
cv2.imwrite('resized.png',resized_image)

#-------------------------

grid_png = cv2.imread('60x60.png', cv2.IMREAD_UNCHANGED)
redSquare = cv2.Canny(grid_png,100,200)
cv2.imshow('edges',redSquare)
(rH, rW) = redSquare.shape[:2]

blueSquare = cv2.imread('resized.png')
(h, w) = blueSquare.shape[:2]

blueSquare = np.dstack([blueSquare, np.ones((h,w), dtype = 'uint8') * 255])
overlay = np.zeros((h,w,4), dtype = 'uint8')
overlay[0:rH, 0:rW] = redSquare
output = blueSquare .copy()
cv2.addWeighted(overlay, 1, output, 1, 0, output)

cv2.imwrite('imageAdded.png', output)


# ------------------------------------


while(True):
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
