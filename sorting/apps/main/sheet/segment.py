'''
Created on Nov 3, 2013

@author: val3xiv
'''
import math
class Segment(object):
    '''
    Element SEGMENT
    '''


    def __init__(self, code = "", 
                 startX = 0.0, startY = 0.0, 
                 endX = 0.0, endY = 0.0, 
                 centerX = None, centerY = None, angle = None, isClockwise = False):
        '''
        Constructor
        '''
        self.code = code
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.centerX = centerX
        self.centerY = centerY
        self.angle = angle
        self.isClockwise = isClockwise
        self.radius = None
        if (self.centerX != None and self.centerY != None):
            self.radius = math.sqrt( (self.centerX - self.startX)**2 + (self.centerY- self.startY)**2 )        

    def __str__(self):        
        myStr = "SEGMENT " + self.code 
        myStr += " (start: " + str(self.startX) + ", " + str(self.startY) 
        myStr += "; end: " + str(self.endX) + ", " + str(self.endY)
        if (self.centerX != None and self.centerY != None):
            myStr += "; centre: " + str(self.centerX) + ", " + str(self.centerY)
            myStr += "; radius: " + str(self.radius)
        if self.angle != None:
            myStr += "; angle: " + str(self.angle)
        if (self.centerX != None and self.centerY != None) or self.angle != None:
            myStr += "; clockwise" if self.isClockwise else ", counter-clockwise"
        myStr += ")\n"
        return myStr
        
