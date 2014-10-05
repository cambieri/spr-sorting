'''
Created on Nov 3, 2013

@author: val3xiv
'''

class Profile(object):
    '''
    Element PROFILE
    '''


    def __init__(self, code = "", isInternal = False, iconDimX = 0.0, iconDimY = 0.0, iconPivotX = 0.0, iconPivotY = 0.0):
        '''
        Constructor
        '''
        self.code = code
        self.isInternal = isInternal
        self.iconDimX = iconDimX
        self.iconDimY = iconDimY
        self.iconPivotX = iconPivotX
        self.iconPivotY = iconPivotY
        self.segments = []
        
    def __str__(self):
        myStr = "PROFILE " + self.code 
        myStr += " (" + ("internal" if self.isInternal else "external")
        myStr += "; icon dimension: " + str(self.iconDimX) + " x " + str(self.iconDimY) 
        myStr += "; icon pivot: " + str(self.iconPivotX) + " x " + str(self.iconPivotY) 
        myStr += ") " + str(len(self.segments)) + " segments\n"
        for myElement in self.segments:
            myStr += "\n".join(("\t") + myLine for myLine in str(myElement).splitlines())        
            myStr += "\n"        
        return myStr
        
    def toSVGpath(self):
        ret = 'd="'
        lastX = None
        lastY = None
        minX = self.iconPivotX - (float(self.iconDimX) / 2)
        minY = self.iconPivotY - (float(self.iconDimY) / 2)
        maxX = self.iconPivotX + (float(self.iconDimX) / 2)
        maxY = self.iconPivotY + (float(self.iconDimY) / 2)
        bbCorners = ""
        bbCorners += "\tM " + str(minX - 1) + ", " + str(minY) + "\n"
        bbCorners += "\tL " + str(minX) + ", " + str(minY) + "\n"
        bbCorners += "\tL " + str(minX) + ", " + str(minY + 1) + "\n"  
        bbCorners += "\tM " + str(maxX) + ", " + str(maxY - 1) + "\n"
        bbCorners += "\tL " + str(maxX) + ", " + str(maxY) + "\n"
        bbCorners += "\tL " + str(maxX - 1) + ", " + str(maxY) + "\n"  
        for mySegment in self.segments:
            if lastX == None and lastY == None:
                ret += bbCorners
                ret += "\tM " + str(mySegment.startX) + ", " + str(mySegment.startY) + "\n"
            if mySegment.centerX == None and mySegment.centerY == None:
                ret += "\tL " + str(mySegment.endX) + ", " + str(mySegment.endY) + "\n"
            else:
                ret += "\tA " + str(mySegment.radius) + ", " + str(mySegment.radius) + ", 0 0,"
                ret += ("0" if mySegment.isClockwise else "1") + " "
                ret += str(mySegment.endX) + ", " + str(mySegment.endY) + "\n"  
            lastX = mySegment.endX     
            lastY = mySegment.endY 
        ret += '"\n'
        return ret
            
    def toRaphaelPath(self):
        ret = ''
        lastX = None
        lastY = None
        minX = self.iconPivotX - (float(self.iconDimX) / 2)
        minY = self.iconPivotY - (float(self.iconDimY) / 2)
        maxX = self.iconPivotX + (float(self.iconDimX) / 2)
        maxY = self.iconPivotY + (float(self.iconDimY) / 2)
        for mySegment in self.segments:
            if lastX == None and lastY == None:
                bbCorners = ""
                bbCorners += "M" + str(minX - 1) + "," + str(minY) + "   "
                bbCorners += "L" + str(minX) + "," + str(minY) + "   "
                bbCorners += "L" + str(minX) + "," + str(minY + 1) + "   "  
                bbCorners += "M" + str(maxX) + "," + str(maxY - 1) + "   "
                bbCorners += "L" + str(maxX) + "," + str(maxY) + "   "
                bbCorners += "L" + str(maxX - 1) + "," + str(maxY) + "   "  
                ret += bbCorners + "M" + str(mySegment.startX) + "," + str(mySegment.startY)
            if mySegment.centerX == None and mySegment.centerY == None:
                ret += "   L" + str(mySegment.endX) + "," + str(mySegment.endY)
            else:
                ret += "   A" + str(mySegment.radius) + "," + str(mySegment.radius) + ",0 1,"
                ret += ("0" if mySegment.isClockwise else "1")
                ret += " "+ str(mySegment.endX - 0.1) + "," + str(mySegment.endY)  
            lastX = mySegment.endX     
            lastY = mySegment.endY 
        return ret

            
        