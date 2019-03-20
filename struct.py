# This Python file uses the following encoding: utf-8
# Cấu trúc của cây STree
# Các class cần thiết trong đề tài
import math
import random
import types
import function

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
    def setVector(self, vector):
        self.__vector = vector

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
            self.cutRoot()
        if (self.root.__class__.__name__ == "Leaf"):
                self.root.add(image)
        else:
            t = self.root
            tempVector = image.getVector()
            lstLink = []
            lstVtLink = []
            lstLink.append(t.id)
            while True:
                direct = function.findMinDistance(tempVector, t.lstVector)
                lstVtLink.append(direct)
                t = function.findNode(t.lstVector[direct], self.lstNode, self.lstLeaf)
                if t.__class__.__name__ == "Leaf":
                    break
                lstLink.append(t.id)
            vt = function.findLeaf(t.id, self.lstLeaf)
            self.lstLeaf[int(vt)].add(image)
            count = 1

            while True:
                node = function.findNodeById(lstLink[len(lstLink) - count], self.lstNode, self.lstLeaf, self.root)
                node.lstVector[int(lstVtLink[len(lstVtLink) - count])].setVector(function.computeAvgVector(node.lstVector))
                count = count + 1
                tempNode = node
                if node == self.root:
                    break

            if self.lstLeaf[int(vt)].n == self.m:
                self.cutLeaf(self.lstLeaf[int(vt)], lstLink, lstVtLink)
                lstLink.reverse()
                lstVtLink.reverse()
                for i in range(0, len(lstLink)):
                    node = function.findNodeById(lstLink[i], self.lstNode, self.lstLeaf, self.root)
                    if node.n < self.m:
                        break
                    else:
                        if (node == self.root):
                            self.cutRoot()
                        else:
                            self.cutNode(node, lstLink[i + 1], lstVtLink[i + 1])

    
    def cutRoot(self):
        if self.root.__class__.__name__ == "Leaf":
            cluster = function.findMaxDistance(self.root.lstImage)
            clusterA = Leaf(self.countId)
            self.countId = self.countId + 1
            clusterA.add(cluster[0])
            clusterB = Leaf(self.countId)
            self.countId = self.countId + 1
            clusterB.add(cluster[1])
            self.lstLeaf.append(clusterA)
            self.lstLeaf.append(clusterB)

            for hog in self.root.lstImage:
                if (int(hog.getId()) == int(cluster[0].getId())):
                    continue
                if (int(hog.getId()) == int(cluster[1].getId())):
                    continue

                if (function.computeDistanceEuclide(hog.getVector(), cluster[0].getVector())
                    < function.computeDistanceEuclide(hog.getVector(), cluster[1].getVector())):
                    clusterA.add(hog)
                else:
                    clusterB.add(hog)
            t = Node(self.root.id)
            self.root = t

            self.root.add(function.computeAvgVector(clusterA.lstImage, clusterA.id))
            self.countId = self.countId + 1
            self.root.add(function.computeAvgVector(clusterB.lstImage, clusterB.id))
            self.countId = self.countId + 1
        else:
            cluster = function.findMaxDistance(self.root.lstVector)
            clusterA = Node(self.countId)
            self.countId = self.countId + 1
            clusterA.add(cluster[0])
            clusterB = Node(self.countId)
            self.countId = self.countId + 1
            clusterB.add(cluster[1])
            self.lstNode.append(clusterA)
            self.lstNode.append(clusterB)

            for v in self.root.lstVector:
                if (int(v.getLink()) == int(cluster[0].getLink())):
                    continue
                if (int(v.getLink()) == int(cluster[1].getLink())):
                    continue

                if (function.computeDistanceEuclide(v.getVector(), cluster[0].getVector())
                    < function.computeDistanceEuclide(v.getVector(), cluster[1].getVector())):
                    clusterA.add(v)
                else:
                    clusterB.add(v)

            t = Node(self.root.id)
            self.root = t
            self.root.add(function.computeAvgVector(clusterA.lstVector, clusterA.id))
            self.countId = self.countId + 1
            self.root.add(function.computeAvgVector(clusterB.lstVector, clusterB.id))
            self.countId = self.countId + 1

    def cutNode(self, node, nodeLink, vtNodeLink):
        cluster = function.findMaxDistance(node.lstVector)
        clusterA = Node(self.countId)
        self.countId = self.countId + 1
        clusterA.add(cluster[0])
        clusterB = Node(self.countId)
        self.countId = self.countId + 1
        clusterB.add(cluster[1])
        self.lstNode.append(clusterA)
        self.lstNode.append(clusterB)
        self.lstNode.remove(node)
        for v in node.lstVector:
            if (int(v.getLink()) == int(cluster[0].getLink())):
                continue
            if (int(v.getLink()) == int(cluster[1].getLink())):
                continue

            if (function.computeDistanceEuclide(v.getVector(), cluster[0].getVector())
                < function.computeDistanceEuclide(v.getVector(), cluster[1].getVector())):
                clusterA.add(v)
            else:
                clusterB.add(v)
        node = function.findNodeById(nodeLink, self.lstNode, self.lstLeaf, self.root)
        node.lstVector.remove(node.lstVector[vtNodeLink])
        node.add(function.computeAvgVector(clusterA.lstVector, clusterA.id))
        node.add(function.computeAvgVector(clusterB.lstVector, clusterB.id))

    def cutLeaf(self, leaf, lstLink, lstVtLink):
        cluster = function.findMaxDistance(leaf.lstImage)
        clusterA = Leaf(self.countId)
        self.countId = self.countId + 1
        clusterA.add(cluster[0])
        clusterB = Leaf(self.countId)
        self.countId = self.countId + 1
        clusterB.add(cluster[1])
        self.lstLeaf.append(clusterA)
        self.lstLeaf.append(clusterB)
        for hog in leaf.lstImage:
            if (int(hog.getId()) == int(cluster[0].getId())):
                continue
            if (int(hog.getId()) == int(cluster[1].getId())):
                continue

            if (function.computeDistanceEuclide(hog.getVector(), cluster[0].getVector())
                < function.computeDistanceEuclide(hog.getVector(), cluster[1].getVector())):
                clusterA.add(hog)
            else:
                clusterB.add(hog)

        count = 1
        node = function.findNodeById(lstLink[len(lstLink) - count], self.lstNode, self.lstLeaf, self.root)
        node.lstVector.remove(node.lstVector[int(lstVtLink[len(lstVtLink) - count])])
        node.add(function.computeAvgVector(clusterA.lstImage, clusterA.id))
        node.add(function.computeAvgVector(clusterB.lstImage, clusterB.id))
        self.lstLeaf.remove(leaf)