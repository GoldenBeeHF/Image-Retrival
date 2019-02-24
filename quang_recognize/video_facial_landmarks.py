# USAGE
# python video_facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat
# python video_facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --picamera 1

# import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import cv2
import os
import math
import time
def computeEuclide(x1, x2, y1, y2):
	return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-r", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())
 
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# initialize the video stream and allow the cammera sensor to warmup
print("[INFO] camera sensor warming up...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

f = open('training.txt', 'a+')
data = f.read()
arr = data.split()
print len(arr)
# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream, resize it to
	# have a maximum width of 400 pixels, and convert it to
	# grayscale
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# detect faces in the grayscale frame
	rects = detector(gray, 0)
	if rects == []:
		continue
	# loop over the face detections
	for rect in rects:
		# determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
	
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
		# loop over the (x, y)-coordinates for the facial landmarks
		# and draw them on the image
		l = int(rect.left() - 20)
		t = int(rect.top() - 20)
		h = int(rect.bottom() - rect.top() + 40)
		w = int(rect.right() - rect.left() + 40)
		crop_img = frame[t:t+h,l:l+w]
		try:
			crop_img = cv2.resize(crop_img, (250, 250), interpolation = cv2.INTER_AREA)
		except:
			continue
		gray_crop = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
		rects_crop = detector(gray_crop, 0)
		for rect_crop in rects_crop:
			shape_crop = predictor(gray_crop, rect_crop)
			shape_crop = face_utils.shape_to_np(shape_crop)
			cv2.rectangle(frame, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 255, 0), 2)
			lstX = []
			lstY = []
			for (x, y) in shape_crop:
				lstX.append(x)
				lstY.append(y)
				
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
			vector.append(computeEuclide(lstX[21], lstX[39], lstY[21], lstY[39]))
			vector.append(computeEuclide(lstX[22], lstX[42], lstY[22], lstY[42]))
			vector.append(computeEuclide(lstX[21], lstX[36], lstY[21], lstY[36]))
			vector.append(computeEuclide(lstX[22], lstX[45], lstY[22], lstY[45]))
			vector.append(computeEuclide(lstX[27], lstX[39], lstY[27], lstY[39]))
			vector.append(computeEuclide(lstX[21], lstX[27], lstY[21], lstY[27]))
			vector.append(computeEuclide(lstX[27], lstX[42], lstY[27], lstY[42]))
			vector.append(computeEuclide(lstX[22], lstX[27], lstY[22], lstY[27]))
			vector.append(computeEuclide(lstX[17], lstX[36], lstY[17], lstY[36]))
			vector.append(computeEuclide(lstX[24], lstX[45], lstY[24], lstY[45]))
			vector.append(computeEuclide(lstX[33], lstX[50], lstY[33], lstY[50]))
			vector.append(computeEuclide(lstX[33], lstX[52], lstY[33], lstY[52]))
			vector.append(computeEuclide(lstX[7], lstX[57], lstY[7], lstY[57]))
			vector.append(computeEuclide(lstX[8], lstX[57], lstY[8], lstY[57]))
			vector.append(computeEuclide(lstX[9], lstX[57], lstY[9], lstY[57]))
			vector.append(computeEuclide(lstX[3], lstX[48], lstY[3], lstY[48]))
			vector.append(computeEuclide(lstX[13], lstX[54], lstY[13], lstY[54]))
			vector.append(computeEuclide(lstX[3], lstX[7], lstY[3], lstY[7]))
			vector.append(computeEuclide(lstX[9], lstX[13], lstY[9], lstY[13]))
			
			loop = int(len(arr) / 42)
			loop_count = 0
			font = cv2.FONT_HERSHEY_SIMPLEX
			isAvailable = False
			for j in range(loop - 1):
				dem = 0
				count_img = 0
				for i in range(42):
					if abs(float(arr[i + loop_count * 42]) - vector[i]) < 6:
						dem = dem + 1
					# print dem
					if dem > 30:
						count_img = count_img + 1
				loop_count = loop_count + 1
				print str(count_img)
				print str(int(loop / 2))
				if count_img > int(loop / 2):
					for (x, y) in shape:
						cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
					cv2.putText(frame,'Quang',(rect.right() - w / 2,rect.bottom()), font, 0.5,(255,0,0),2,cv2.LINE_AA)
					isAvailable = True
					break
			if isAvailable == False:	
				cv2.putText(frame,'Unknown',(rect.right() - w / 2,rect.bottom()), font, 0.5,(255,0,0),2,cv2.LINE_AA)

				
	  
	# show the frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()