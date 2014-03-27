'''
Created on Mar 19, 2014

@author: val3xiv
'''
import os
import ConfigParser
import math
import datetime

class Tools(object):
    '''
    Generic functions
    '''


    def __init__(self):
        self.isLogging = False
        '''
        Empty constructor
        '''
    def readIniFile(self, fileToRead):
        ret = None
        if (os.path.isfile(fileToRead)):
            ret = {}
            myConfig = ConfigParser.ConfigParser()
            myConfig.read(fileToRead)
            for mySection in myConfig.sections():
                mySectionName = mySection.lower().strip()
                for myOption in myConfig.options(mySection):
                    ret[mySectionName + "." + myOption.lower().strip()] = myConfig.get(mySection, myOption).strip()
        return ret if (ret != None and len(ret)) > 0 else None
    
    def rotatePoint(self, point, angleDegrees):
        angleRadians = math.radians(angleDegrees)
        x1 = math.cos(angleRadians) * point[0] - math.sin(angleRadians) * point[1] 
        y1 = math.sin(angleRadians) * point[0] + math.cos(angleRadians) * point[1]
        return (x1, y1)
    
    def printLog(self, agent, listMessages):
        while self.isLogging:                    
            pass
        self.isLogging = True
        print "\n[" + str(datetime.datetime.now()) + "] " + agent
        for myMessage in listMessages:
            print str(myMessage)
        self.isLogging = False
    
    if __name__ == '__main__':
        x = 90
        y = 110
        (x,y) = rotatePoint(None, (x, x), 10)
        print (x,y)
    