
import cv2
import os
import sys
import numpy as np
import random
from math import trunc
from scipy import ndimage


def brightness(image, value=50):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img



def darkness(image, value=50):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    
    lim = value
    v[v > lim] -= value
    v[v <= lim] = 0
    
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


for i in range(1,11):
    img = cv2.imread("Record" + str(i) + ".jpg")
    image1 = ndimage.rotate(img, 45)
    image2 = darkness(img, 50)
    image3 = brightness(img, 50)
    cv2.imwrite("Record" + str(i) + "rotated" + ".jpg",image1)
    cv2.imwrite("Record" + str(i) + "darkened" + ".jpg",image2)
    cv2.imwrite("Record" + str(i) + "brightened" + ".jpg",image3)
    



