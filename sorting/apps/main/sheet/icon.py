'''
Created on Nov 3, 2013

@author: val3xiv
'''

class Icon(object):
    '''
    Element ICON
    '''


    def __init__(self, code = "", 
                 dimX = 0.0, dimY = 0.0, 
                 pivotX = 0.0, pivotY = 0.0, 
                 barycentreX = 0.0, barycentreY = 0.0, 
                 area = 0.0, 
                 isScrap = False, isLabel = False):
        '''
        Constructor
        '''
        self.code = code.replace("\\", "").replace("/", "")
        self.dimX = dimX
        self.dimY = dimY
        self.pivotX = pivotX
        self.pivotY = pivotY
        self.barycentreX = barycentreX
        self.barycentreY = barycentreY
        self.area = area
        self.isScrap = isScrap
        self.isLabel = isLabel
        self.profiles = []
        
    def __str__(self):
        myStr = "ICON " + self.code 
        myStr += " (dimension: " + str(self.dimX) + " x " + str(self.dimY) 
        myStr += "; pivot: " + str(self.pivotX) + ", " + str(self.pivotY) 
        myStr += "; barycentre: " + str(self.barycentreX) + ", " + str(self.barycentreY)
        myStr += "; area: " + str(self.area)
        myStr += "; scrap" if self.isScrap else "" 
        myStr += "; label" if self.isLabel else "" 
        myStr += ") " + str(len(self.profiles)) + " profiles\n"
        for myElement in self.profiles:
            myStr += "\n".join(("\t") + myLine for myLine in str(myElement).splitlines())        
            myStr += "\n"        
        return myStr
        