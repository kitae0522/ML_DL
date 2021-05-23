import cv2
import os
import numpy as np

path = "C:\guide"

file_list = os.listdir(path)

for k in file_list:
    img = cv2.imread(path + '\\' + k)
    width, height = img.shape[:2]
    resize_img = cv2.resize(img, (416, 416), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('C:\guide_resize\\' + k, resize_img)
