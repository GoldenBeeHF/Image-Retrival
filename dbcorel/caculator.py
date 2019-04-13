import cv2
from pixel import Pixel 
image = cv2.imread("img.jpg")
p = image.shape

rows,cols, chanels = image.shape

listPixel = []
for i in range(rows):
    for j in range(cols):
        listPixel.append(image[i,j])
        

arrVector = []

for i in range(25):
        arrVector.append(0)

listPixelColor = []

listPixelColor.append(Pixel([0, 0, 0])) #black
listPixelColor.append(Pixel([0, 182, 0])) #seagreen
listPixelColor.append(Pixel([170, 255, 0])) #lightgreen
listPixelColor.append(Pixel([0, 73, 36])) #lightgreen
listPixelColor.append(Pixel([170, 146, 36])) #Aqua
listPixelColor.append(Pixel([0, 255, 36])) #Bright Green
listPixelColor.append(Pixel([170, 36, 73])) #Blue
listPixelColor.append(Pixel([0, 146, 73])) #Green
listPixelColor.append(Pixel([170, 219, 73])) #Turquoise
listPixelColor.append(Pixel([0, 36, 109])) #Brown
listPixelColor.append(Pixel([170, 109, 109])) #Blue Gray
listPixelColor.append(Pixel([0, 219, 109])) #Lime
listPixelColor.append(Pixel([170, 0, 146])) #Lavender
listPixelColor.append(Pixel([0, 109, 146])) #Plum
listPixelColor.append(Pixel([170, 182, 146])) #Teal
listPixelColor.append(Pixel([0, 0, 182])) #Dark Red
listPixelColor.append(Pixel([170, 73, 182])) #Magenta
listPixelColor.append(Pixel([0, 182, 182])) #Yellow Green
listPixelColor.append(Pixel([170, 255, 182])) #Flouro Green
listPixelColor.append(Pixel([0, 73, 219])) #Red
listPixelColor.append(Pixel([170, 146, 219])) #Rose
listPixelColor.append(Pixel([0, 255, 219])) #Yellow
listPixelColor.append(Pixel([170, 36, 255])) #Pink
listPixelColor.append(Pixel([0, 146, 255])) #Orange
listPixelColor.append(Pixel([255, 255, 255])) #White 

for j in range(len(listPixel)):
    listPixelColor.__getitem__(0).distanceEuclide(listPixel[j])
    min   = listPixelColor.__getitem__(0).getRatio()
    index = 0
    for i in range(len(listPixelColor)):
        listPixelColor.__getitem__(i).distanceEuclide(listPixel[j])
        if(min > listPixelColor.__getitem__(i).getRatio()):
            min   = listPixelColor.__getitem__(i).getRatio()
            index = i
    arrVector[index] += 1    

for i in range(len(arrVector)):
        if (arrVector[i] != 0) : arrVector[i] = float(arrVector[i]) / (cols * rows)

