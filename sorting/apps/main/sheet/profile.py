'''
Created on Nov 3, 2013

@author: val3xiv
'''

class Profile(object):
    '''
    Element PROFILE
    '''


    def __init__(self, code = "", isInternal = False):
        '''
        Constructor
        '''
        self.code = code
        self.isInternal = isInternal
        self.segments = []
        
    def __str__(self):
        myStr = "PROFILE " + self.code + " (" + ("internal" if self.isInternal else "external")
        myStr += ") " + str(len(self.segments)) + " segments\n"
        for myElement in self.segments:
            myStr += "\n".join(("\t") + myLine for myLine in str(myElement).splitlines())        
            myStr += "\n"        
        return myStr
        
    def toSVGpath(self):
        ret = 'd="'
        lastX = None
        lastY = None
        for mySegment in self.segments:
            if lastX == None and lastY == None:
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
        for mySegment in self.segments:
            if lastX == None and lastY == None:
                ret += "M" + str(mySegment.startX) + "," + str(mySegment.startY)
            if mySegment.centerX == None and mySegment.centerY == None:
                ret += "   L" + str(mySegment.endX) + "," + str(mySegment.endY)
            else:
                ret += "   A" + str(mySegment.radius) + "," + str(mySegment.radius) + ",0 1,"
                ret += ("0" if mySegment.isClockwise else "1")
                ret += " "+ str(mySegment.endX - 0.1) + "," + str(mySegment.endY)  
            lastX = mySegment.endX     
            lastY = mySegment.endY 
        return ret

            
        