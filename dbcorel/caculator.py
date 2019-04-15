import cv2
<<<<<<< HEAD
from pixel import Pixel
=======
import math
>>>>>>> master
image = cv2.imread("img.jpg")
p = image.shape

rows,cols, chanels = image.shape

listPixel = []
lenListPixel = 0
for i in range(rows):
    for j in range(cols):
        listPixel.append(image[i,j])
        lenListPixel += 1
        
arrVector = []

for i in range(25):
        arrVector.append(0)

listPixelColor = []

listPixelColor.append([0, 0, 0]) #black
listPixelColor.append([0, 182, 0]) #seagreen
listPixelColor.append([170, 255, 0]) #lightgreen
listPixelColor.append([0, 73, 36]) #lightgreen
listPixelColor.append([170, 146, 36]) #Aqua
listPixelColor.append([0, 255, 36]) #Bright Green
listPixelColor.append([170, 36, 73]) #Blue
listPixelColor.append([0, 146, 73]) #Green
listPixelColor.append([170, 219, 73]) #Turquoise
listPixelColor.append([0, 36, 109]) #Brown
listPixelColor.append([170, 109, 109]) #Blue Gray
listPixelColor.append([0, 219, 109]) #Lime
listPixelColor.append([170, 0, 146]) #Lavender
listPixelColor.append([0, 109, 146]) #Plum
listPixelColor.append([170, 182, 146]) #Teal
listPixelColor.append([0, 0, 182]) #Dark Red
listPixelColor.append([170, 73, 182]) #Magenta
listPixelColor.append([0, 182, 182]) #Yellow Green
listPixelColor.append([170, 255, 182]) #Flouro Green
listPixelColor.append([0, 73, 219]) #Red
listPixelColor.append([170, 146, 219]) #Rose
listPixelColor.append([0, 255, 219]) #Yellow
listPixelColor.append([170, 36, 255]) #Pink
listPixelColor.append([0, 146, 255]) #Orange
listPixelColor.append([255, 255, 255]) #White 


def distanceEuclide(pixelColor, pixelImage):
	return math.sqrt(math.pow(pixelColor[0] - pixelImage[0], 2) + math.pow(pixelColor[1] - pixelImage[1], 2) + math.pow(pixelColor[2] - pixelImage[2], 2))

for j in range(lenListPixel):
    min   = distanceEuclide(listPixel[j],listPixelColor[i])
    index = 0
    for i in range(25):
        temp = distanceEuclide(listPixel[j],listPixelColor[i])
        if(min > temp ):
            min   =  temp
            index = i
    arrVector[index] += 1    

for i in range(25):
        if (arrVector[i] != 0) : arrVector[i] = float(arrVector[i]) / (cols * rows)

print(arrVector)