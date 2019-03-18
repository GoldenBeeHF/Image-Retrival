# This Python file uses the following encoding: utf-8
# Task tạo cây STree cải thiện tốc độ tìm kiếm hình ảnh của khóa luận
# Người thực hiện: Trần Lê Văn Đức
# Thời gian thực hiện: đến hết thứ 4, ngày 13 tháng 3 năm 2019
# Yêu cầu làm việc nghiêm túc !!!

# Các bước tạo cây:
# B1: Tạo nút root của cây. Thêm hình (HOG) đầu tiên vào. Cho sức chứa là 20 (quá 20 sẽ tách nút).
# B2: Thêm lần lượt các hình tiếp theo vào. Khi vượt quá 20 sẽ tách nút.
# Cách tách: chọn 2 vector xa nhau nhất tạo thành 2 nút. Đưa các vector còn lại vào 2 nút vừa tạo
# Quy tắc: gần nút nào sẽ gom vào nút đó.
# B3: Sau đó tính vector trung bình của mỗi nút.
# Cách tính: cộng tuyến tính các thành phần của vector sau đó chia trung bình
# Vd: v1 = (x1, x2, ..., xN), v2 = (y1, y2, ..., yN)
# vTB = ((x1 + y1) / 2, (x2 + y2) / 2, ..., (xN + yN) / 2)
# B4: Tạo nút mới với các phần tử là 2 vector trung bình vừa tính. Link 2 vector trung bình với nút con.
# B5: Tiếp tục thêm hình vào cây.
# Cách thêm: mỗi hình đưa vào sẽ so sánh với 2 vector trung bình vừa tạo xem gần vector nào hơn.
# Sau đó sẽ theo đường link và thêm xuống nút lá.
# Khi thêm xuống nút lá phải tiến hành tính lại vector trung bình.
# Cứ tiếp tục thêm đến khi tràn nút lá thì lại tiếp tục tách nút.
# 2 vector trung bình lấy được sẽ được thêm vào root.
# Khi nút root tràn sẽ tách nút root. Tương tự làm tiếp tục.

import math
import random
import types

# Cấu trúc của 1 hình: gồm vector và id
class HOG:
    def __init__(self, vector, idImage):
        self.__vector = vector # private attribute
        self.__id = idImage # private attribute
    def getId(self):
        return self.__id
    def getVector(self):
        return self.__vector

class Vector:
    def __init__(self, vector, link):
        self.__vector = vector # private attribute
        self.__link = link # private attribute
    def getVector(self):
        return self.__vector
    def getLink(self):
        return self.__link

# Cấu trúc của 1 nút lá gồm:
# + n: số lượng phần tử
# + lstVector: danh sách các hình (class HOG)
class Leaf:
    def __init__(self, idLeaf):
        self.id = idLeaf
        self.n = 0
        self.lstImage = []
    
    def add(self, image):
        self.lstImage.append(image)
        self.n = self.n + 1

# Cấu trúc của 1 nút không phải lá trong cây:
# + n: số lượng phần tử
# + link: link tới nút con
# + lstVector: danh sách các vector (mỗi vector là 1 mảng 42 phần tử)
class Node:
    def __init__(self, idNode):
        self.id = idNode
        self.n = 0
        self.lstVector = []

    def add(self, vector):
        self.lstVector.append(vector)
        self.n = self.n + 1

    def setLink(self, link):
        self.link = link

# Cấu trúc cây STree:
# + root: nút gốc
# + lstLeaf: danh sách các nút lá
# + lstNode: danh sách các nút không phải lá và root trong cây

def computeDistanceEuclide(vectorA, vectorB):
    dis = 0
    for i in range(0, len(vectorA)):
        dis = dis + math.pow(vectorA[i] - vectorB[i], 2)
    return math.sqrt(dis)

# return 2 vector with max distance
def findMaxDistance(lstVector):
    max = computeDistanceEuclide(lstVector[0].getVector(), lstVector[1].getVector())
    vector1 = lstVector[0]
    vector2 = lstVector[1]
    for i in range(0, len(lstVector) - 1):
        for j in range(i + 1, len(lstVector)):
            if (max < computeDistanceEuclide(lstVector[i].getVector(), lstVector[j].getVector())):
                max = computeDistanceEuclide(lstVector[i].getVector(), lstVector[j].getVector())
                vector1 = lstVector[i]
                vector2 = lstVector[j]
    return [vector1, vector2]

def computeAvgVector(lstVector, idVector):
    n = 5
    avgVector = []
    for i in range(0, n):
        avgVector.append(0)
    for v in lstVector:
        for i in range(0, n):
            avgVector[i] = avgVector[i] + v.getVector()[i]

    for i in range(0, n):
        avgVector[i] = avgVector[i] / len(lstVector)
    
    return Vector(avgVector, idVector)

def findNode(idNode, lstNode, lstLeaf):
    for node in lstNode:
        if int(idNode.getLink()) == int(node.id):
            return node
    for node in lstLeaf:
        if int(idNode.getLink()) == int(node.id):
            return node
    return None

def findMinDistance(node, lstNode):
    vt = 0
    min = computeDistanceEuclide(node, lstNode[0].getVector())
    for i in range(1, len(lstNode)):
        if min > computeDistanceEuclide(node, lstNode[i].getVector()):
            min = computeDistanceEuclide(node, lstNode[i].getVector())
            vt = i
    return vt

def findLeaf(idLeaf, lstLeaf):
    print idLeaf, lstLeaf[0].id, lstLeaf[1].id
    for i in range (0, len(lstLeaf)):
        if int(idLeaf) == int(lstLeaf[i].id):
            print i
            return i

class STree:
    def __init__(self):
        self.m = 20
        self.countId = 0
        self.root = None
        self.lstLeaf = []
        self.lstNode = []

    def addRoot(self, root):
        self.root = root

    def addImage(self, image):
        if (self.root.n == self.m):
            self.cut(self.root)
            print self.root.lstVector[0].getLink(), self.root.lstVector[0].getVector()
            print self.root.lstVector[1].getLink(), self.root.lstVector[1].getVector()
        if (self.root.__class__.__name__ == "Leaf"):
                self.root.add(image)
        else:
            t = self.root
            tempVector = image.getVector()
            while True:
                direct = findMinDistance(tempVector, t.lstVector)
                t = findNode(t.lstVector[direct], self.lstNode, self.lstLeaf)
                print t.__class__.__name__
                print t.id
                if t.__class__.__name__ == "Leaf":
                    break
            vt = findLeaf(t.id, self.lstLeaf)
            self.lstLeaf[int(vt)].add(image)
            
            for leaf in self.lstLeaf:
                print "Cluster"
                for image in leaf.lstImage:
                    print image.getId(), image.getVector()
    
    def cut(self, node):
        if (node == self.root):
            cluster = findMaxDistance(self.root.lstImage)
            clusterA = Leaf(self.countId)
            self.countId = self.countId + 1
            clusterA.add(cluster[0])
            clusterB = Leaf(self.countId)
            self.countId = self.countId + 1
            clusterB.add(cluster[1])
            self.lstLeaf.append(clusterA)
            self.lstLeaf.append(clusterB)

            for hog in node.lstImage:
                if (int(hog.getId()) == int(cluster[0].getId())):
                    continue
                if (int(hog.getId()) == int(cluster[1].getId())):
                    continue

                if (computeDistanceEuclide(hog.getVector(), cluster[0].getVector())
                    < computeDistanceEuclide(hog.getVector(), cluster[1].getVector())):
                    clusterA.add(hog)
                else:
                    clusterB.add(hog)
            t = Node(self.root.id)
            self.root = t

            self.root.add(computeAvgVector(clusterA.lstImage, clusterA.id))
            self.countId = self.countId + 1
            self.root.add(computeAvgVector(clusterB.lstImage, clusterB.id))
            self.countId = self.countId + 1
            # print "Cluster A"
            # for v in clusterA.lstImage:
            #     print v.getId(), v.getVector()
            
            # print "Cluster B"
            # for v in clusterB.lstImage:
            #     print v.getId(), v.getVector()

lst = []
for i in range(0, 30):
    vector = [
        random.randint(1, 100), 
        random.randint(1, 100), 
        random.randint(1, 100), 
        random.randint(1, 100), 
        random.randint(1, 100)
    ]
    
    a = HOG(vector, i)
    lst.append(a)

tree = STree()
tree.root = Leaf(tree.countId)
tree.countId = tree.countId + 1

for image in lst:
    tree.addImage(image)

