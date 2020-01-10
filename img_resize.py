# import numpy as np
import cv2 as cv
img = cv.imread('testObj143.jpg')
input_std=255
height, width = img.shape[:2]
res = cv.resize(img,(299, 299), interpolation = cv.INTER_LINEAR)
# normalized = res/input_std
# print(normalized)
cv.imshow('original',img)
cv.imshow('resized',res)
# cv.imshow('normalized',normalized)
cv.imwrite('143resized.jpg',res)
cv.waitKey(0)