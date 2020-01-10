import math
import numpy as np
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*6,3), np.float32)

objp[:,:2] = np.mgrid[0:6,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
DATA_DIR = "C:/Users/kumar_vaibhav/PycharmProjects/CameraCalibration/data_ELP_1024x768/"

images = glob.glob(DATA_DIR+'*.jpg')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (6,6),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (6,6), corners2,ret)
        # cv2.imshow('img',img)
        # if cv2.waitKey() & 0xFF == ord('q'):
        #     break

cv2.destroyAllWindows()


ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,cv2.CALIB_USE_INTRINSIC_GUESS)
# ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
print('ret:',ret)
print('Camera Matrix:',mtx)
print('Distortion Coefficients:',dist)
print('Rotation Vector:',rvecs)
print('Translation Vector:',tvecs)

# img = cv2.imread('C:/Users/kumar_vaibhav/PycharmProjects/CameraCalibration/data_ELP_1024x768/WIN_20190426_11_31_40_Pro.jpg')
# h,  w = img.shape[:2]
# newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
# print('new Camera Matrix:',newcameramtx)

# CMOS_DIAGONAL is the CMOS diagonal length of the camera used.
# Here the CMOS diagonal size is 5.7 mm.
CMOS_DIAGONAL = 5.7
IMAGE_WIDTH = 1024
IMAGE_HEIGHT = 768
# CMOS_width^2 + CMOS_height^2 = CMOS_DIAGONAL^2
CMOS_width = CMOS_height = math.sqrt(CMOS_DIAGONAL*CMOS_DIAGONAL/2)

# Fx can be calculated in mm using the formula:
# Fx = fx * (W/w)
# where fx is the focal length (width) in pixels
# W is the width of CMOS
# w is the image width in pixels

Fx = mtx[0][0]*(CMOS_width/IMAGE_WIDTH)
Fy = mtx[1][1]*(CMOS_height/IMAGE_HEIGHT)
print('Focal length,Fx:',Fx,'mm')
print('Focal length,Fx:',Fy,'mm')

