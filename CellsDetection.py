import numpy as np
import os
import cv2

pathToImages = "/home/slobodanka/pic/"
images = []
for imgName in os.listdir(pathToImages):
    print("pathToImages", pathToImages, imgName)
    im = cv2.imread(os.path.join(pathToImages,imgName))
    if im is not None:
        images.append(im)
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])
        # adaptive threshold
        # Threshold the HSV image to get only blue colors
        maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)

        maskBlueResized = cv2.resize(maskBlue, (650, 650))
        cv2.imshow('mask', maskBlueResized)

        image, contours, hierarchy = cv2.findContours(maskBlue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        print('\n\ncontours', contours)
        print(len(contours))

        cv2.drawContours(im, contours, -1, (0, 255, 0), 2)
        imS = cv2.resize(im, (650, 650))
        cv2.imshow("Contour", imS)

        # define range of red color in HSV
        #lower_red = np.array([0, 100, 100])
        #upper_red = np.array([20, 255, 255])

        # Threshold the HSV image to get only blue colors
        #maskRed = cv2.inRange(hsv, lower_red, upper_red)
        #maskRedResized = cv2.resize(maskRed, (650, 650))
        #cv2.imshow('mask2', maskRedResized)
        #image, contours, hierarchy = cv2.findContours(maskRed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(im, contours, -1, (0, 255, 0), 2)
        #imS = cv2.resize(im, (650, 650))
        #cv2.imshow("Contour2", imS)

        cv2.waitKey()
