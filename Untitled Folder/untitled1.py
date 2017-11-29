import numpy as np
import cv2

#read image

img = cv2.imread('paris.jpg',IMREAD_COLOR)

px = img[53,55]

img[53,55]=[255,255,255]

print(px)

img[100:150,100:150] = [0,0,255]

print(img.shape)
print(img.size)
print(img.dtype)

cv2.imshow('sd',img)
cv2.waitkey()
cv2.destroyAllWindows()