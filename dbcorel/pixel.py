import math

class Pixel:
    #filed
    Color = []
    ratio = 1.5
    
    def __init__(self, Color):
        self.Color = Color

    def distanceEuclide(self, pixelImage):
		self.ratio = math.sqrt(math.pow(self.Color[0] - pixelImage[0], 2) + math.pow(self.Color[1] - pixelImage[1], 2) + math.pow(self.Color[2] - pixelImage[2], 2))
    def getRatio(self):
        return self.ratio
    def getColor(self):
        return self.Color
    #  def distanceEuclide(Color, pixelImage):
	# 	self.ratio = math.sqrt(math.pow(Color[0] - pixelImage[0], 2) + math.pow(self[1] - pixelImage[1], 2) + Math.pow(self[2] - pixelImage[2], 2))
    
