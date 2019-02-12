import numpy as np
import cv2 as cv
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import math

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
        help="path to facial landmark predictor")
args = vars(ap.parse_args())

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

face_cascade = cv.CascadeClassifier('E:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_alt.xml')
img = cv.imread('C:\\Users\\Dell7559\\Desktop\\0.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def computeEuclide(x1, x2, y1, y2):
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

rects = detector(gray, 0)

for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        lstX = []
        lstY = []
        for (x, y) in shape:
                cv.circle(img, (x, y), 1, (0, 0, 255), -1)
                lstX.append(x)
                lstY.append(y)

        # for i in range(0, len(lstX)):
        #         print lstX[i], " ", lstY[i]

        vector = []

        vector.append(computeEuclide(lstX[0], lstX[16], lstY[0], lstY[16]))
        vector.append(computeEuclide(lstX[36], lstX[39], lstY[36], lstY[39]))
        vector.append(computeEuclide(lstX[42], lstX[45], lstY[42], lstY[45]))
        vector.append(computeEuclide(lstX[39], lstX[42], lstY[39], lstY[42]))
        vector.append(computeEuclide(lstX[31], lstX[35], lstY[31], lstY[35]))
        vector.append(computeEuclide(lstX[48], lstX[54], lstY[48], lstY[54]))
        vector.append(computeEuclide(lstX[19], lstX[39], lstY[19], lstY[39]))
        vector.append(computeEuclide(lstX[24], lstX[42], lstY[24], lstY[42]))
        vector.append(computeEuclide(lstX[19], lstX[36], lstY[19], lstY[36]))
        vector.append(computeEuclide(lstX[24], lstX[45], lstY[24], lstY[45]))
        vector.append(computeEuclide(lstX[19], lstX[24], lstY[19], lstY[24]))
        vector.append(computeEuclide(lstX[31], lstX[39], lstY[31], lstY[39]))
        vector.append(computeEuclide(lstX[35], lstX[42], lstY[35], lstY[42]))
        vector.append(computeEuclide(lstX[33], lstX[39], lstY[33], lstY[39]))
        vector.append(computeEuclide(lstX[33], lstX[42], lstY[33], lstY[42]))
        vector.append(computeEuclide(lstX[31], lstX[33], lstY[31], lstY[33]))
        vector.append(computeEuclide(lstX[33], lstX[35], lstY[33], lstY[35]))
        vector.append(computeEuclide(lstX[31], lstX[51], lstY[31], lstY[51]))
        vector.append(computeEuclide(lstX[35], lstX[51], lstY[35], lstY[51]))
        vector.append(computeEuclide(lstX[31], lstX[48], lstY[31], lstY[48]))
        vector.append(computeEuclide(lstX[35], lstX[54], lstY[35], lstY[54]))
        vector.append(computeEuclide(lstX[8], lstX[48], lstY[8], lstY[48]))
        vector.append(computeEuclide(lstX[8], lstX[54], lstY[8], lstY[54]))

        for i in range(0, len(vector)):
                print vector[i]

cv.imshow("Img", img)

cv.waitKey(0)
cv.destroyAllWindows()