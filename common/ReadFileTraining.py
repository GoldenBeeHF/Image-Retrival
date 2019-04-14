# This file convert training file to array vector

# open file training. File training is store in the same folder with this file.
f = open('training.txt')

# read file training
string = f.read()

# split result read file training with blank
data = string.split(' ')

arrVector = []

# Length of vector histogram
lengthVector = 25

# number of iterations of for
numberOfIterations = len(data) / lengthVector

for i in range(0, numberOfIterations):
    vector = []
    for j in range(0, lengthVector):
        vector.append(data[j * i])
    arrVector.append(vector)

print len(arrVector)
print arrVector[0]
