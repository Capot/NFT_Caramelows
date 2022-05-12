import cv2 as cv
import numpy as np
import random as rd

# Load two images
img1 = cv.imread('frita.jpg')
img2 = cv.imread('chapeu.png')

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

dst = cv.add(img1,img2)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
cv.waitKey()
