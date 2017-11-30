import cv2
import numpy as np
#import imutils
class processor:
	try:

		image = raw_input('select map number for Pre-processing : ')
		img = cv2.imread('unedited_map/'+image+'.png')

		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		kernel = np.ones((5,5), np.uint8)

		lower = np.array([115, 118, 118])
		upper = np.array([150, 170, 170])

		#------------------procssing---------------

		mask = cv2.inRange(hsv, lower, upper)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

		img_dilate = cv2.dilate(mask, kernel, iterations=2)
		imag_dilate = cv2.dilate(img_dilate, kernel, iterations=2)

		#ret,thresh1 = cv2.threshold(img_dilate,110,255,cv2.THRESH_BINARY_INV)
		#img_erosion = cv2.erode(img_dilate, kernel, iterations=1)
		opening = cv2.morphologyEx(img_dilate, cv2.MORPH_OPEN, kernel)

		#------------------output-for reference-------------
		#
		# cv2.imshow('image', img)
		# cv2.imshow('mask', mask)
		# cv2.imshow('dilation', img_dilate)
		# cv2.imshow('noiseless',opening)
		# cv2.imshow('dilation2', imag_dilate)


		#---------------Rescaling of image-----------

		resized_image = cv2.resize(img_dilate,(2222,2229))

		#-----------------save image-----------
		cv2.imwrite('processed/processed_map_'+image+'.png',resized_image)

		#--------------------------------
	except :
		pass
