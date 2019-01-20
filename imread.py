import cv2 as cv
import numpy as np


def get_image_infor(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


def video_demo():
    cap =cv.VideoCapture(0)
    while(True):
        rat, frame =cap.read()
        frame =cv.flip(frame,1)
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('frame',gray)
        cv.waitKey(50)

src=cv.imread('E:/demo/images/cat.jpg')
cv.namedWindow('input image')
cv.imshow('input image',src)
get_image_infor(src)
video_demo()
cv.waitKey(0)
cv.destroyAllWindows()

