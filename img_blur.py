import cv2
import numpy as np
from glob import glob
import os

def main():
    base_folder = 'Images'
    sub_folder = 'Person/Test'
    path_of_image = os.path.join(base_folder, sub_folder)
    filtered_folder = 'Filtered_Person'
    path_of_filtered_image = os.path.join(base_folder, filtered_folder)
    if not os.path.exists(path_of_filtered_image):
        os.makedirs(path_of_filtered_image)

    kernel = np.ones((5, 5), np.float32) / 25
    img_names = glob(os.path.join(path_of_image,'*.jpg'))
    img_list = []
    for filename in os.listdir(path_of_image):
        img_list.append(filename)
    # print(img_list)
    count = 0
    for filename in img_names:
        img = cv2.imread(str(filename))
        dst = cv2.filter2D(img, -1, kernel)
        # print(os.path.join(path_of_filtered_image, img_list[count]))
        cv2.imwrite(os.path.join(path_of_filtered_image, img_list[count]), dst)
        count = count + 1

    print("Done.")

if __name__ == '__main__':
    # Calling main() function
    main()









#
# img = cv2.imread('lenna.jpg')
#
# kernel = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernel)
#
# cv2.imshow('Original',img)
# cv2.imshow('Average',dst)
