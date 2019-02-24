import cv2
import sys
import dlib
import copy
import argparse
from imutils import face_utils
import numpy
import math
import os
def computeEuclide(x1, x2, y1, y2):
	return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
    help="path to facial landmark predictor")
ap.add_argument("-f", "--folder-train", required=True,
    help="path folder training")
ap.add_argument("-dst", "--dst-folder", required=True,
    help="path destination folder")

args = vars(ap.parse_args())

video_capture = cv2.VideoCapture(0)

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])
dem = 0
dstFolder = args["dst_folder"]

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

path = args["folder_train"]
allfiles = os.listdir(path)

# print allfiles

f1 = open('C:\\Users\\Dell7559\\Desktop\\training.txt', 'a+')

data = []
for file in allfiles:
    data.append(path + "\\" + file)

arrLocation = []
for s in range(len(data)):
    arrLocation.append(os.path.basename(os.path.splitext(data[s])[0]))

arrLocation = map(int, arrLocation)
arrLocation.sort()

for i in range(len(arrLocation)):
    img = cv2.imread(path + "\\" + str(arrLocation[i]) + ".jpg")
    img = cv2.resize(img, (400, 400), interpolation = cv2.INTER_AREA)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    if rects == []:
		continue
    for rect in rects:
		# determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        
        l = int(rect.left() - 20)
        t = int(rect.top() - 20)
        h = int(rect.bottom() - rect.top() + 40)
        w = int(rect.right() - rect.left() + 40)
        crop_img = img[t:t+h,l:l+w]
        try:
            crop_img = cv2.resize(crop_img, (250, 250), interpolation = cv2.INTER_AREA)
        except:
            continue

        gray_crop = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        rects_crop = detector(gray_crop, 0)
        for rect_crop in rects_crop:
            shape_crop = predictor(gray_crop, rect_crop)
            shape_crop = face_utils.shape_to_np(shape_crop)
            cv2.rectangle(crop_img, (rect_crop.left(), rect_crop.top()), (rect_crop.right(), rect_crop.bottom()), (0, 255, 0), 2)
            for (x, y) in shape_crop:
                cv2.circle(crop_img, (x, y), 1, (0, 0, 255), -1)
    
    cv2.imshow("image", crop_img)
    cv2.waitKey(0)
 


