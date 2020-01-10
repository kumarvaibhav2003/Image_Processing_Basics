import cv2

img = cv2.imread("lenna.jpg")
x = 0
y = 0
[rows,cols,channels]=img.shape
w = 150
h = 150
print('Height:',rows)
print('Width:',cols)
print('channels:',channels)
crop_img = img[y:int(rows/2), x:int(cols/2)]
cv2.imshow('Original Image',img)
cv2.imshow('my crop',crop_img)
cv2.waitKey(0)
