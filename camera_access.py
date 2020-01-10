import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
# cap.set(cv2.CAP_PROP_EXPOSURE, -17.0)
# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
# print(cap.get(cv2.CAP_PROP_EXPOSURE))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'H264')
# fourcc = cv2.VideoWriter_fourcc(*'X264')
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')

# out = cv2.VideoWriter('output.mp4',fourcc, 15.0, (1280,720))
out = cv2.VideoWriter('output.avi',fourcc, 15.0, (640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()