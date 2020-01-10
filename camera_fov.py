import numpy as np
import cv2

cap = cv2.VideoCapture(0)
_DEFAULT_SENSOR_SIZE = (6.0, 4.8)   # mm
#Rotation Vector
rvec = np.array([0, 0, 0], np.float)

# Translation Vector
tvec = np.array([0, 0, 0], np.float)

# fx and fy are the focal lengths expressed in pixel units.
fx = fy = 1.0
# (cx,cy) is a principal point that is usually at the image center.
cx = cy = 0.0

cameraMatrix = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
ret, frame = cap.read()
[rows, cols, channels] = frame.shape

aperture = _DEFAULT_SENSOR_SIZE

# print('aperture_width:',aperture[0])
# print('aperture_height:',aperture[1])
fov_x, fov_y, focal_len, principal, aspect = \
            cv2.calibrationMatrixValues(cameraMatrix, (cols,rows),
                                        aperture[0], aperture[1])

print('fov_x:',fov_x)
print('fov_y:',fov_y)
print('focal length',focal_len)
print('principal:',principal)
print('aspect:',aspect)


# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()