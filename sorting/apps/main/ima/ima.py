'''
Created on Nov 2, 2013

@author: val3xiv
'''
import os.path
import math
from _enum import Enum
from call import Call
from part import Part
from profile import Profile
from main.sheet import sheet, profile, segment
from main.sheet.icon import Icon
from main.sheet.position import Position

class Ima(object):
    '''
    Element IMA
    '''

    def __init__(self, filePathInput = None, filePathOutput = None, isDebug = False):
        '''
        Constructor
        '''
        self.isDebug = isDebug
        self._map = {"Program" : "programName",
                     "Mat" : "material",
                     "Thk" : "thickness",
                     "FormatCode" : "formatCode",
                     "DimX" : "dimX",
                     "DimY" : "dimY"}
        self.__filePath = ""
        self.__clear()
        self.filePath = filePathInput
        self.outputFile = filePathOutput

    def get_thickness(self):
        return self.__thickness

    def get_dim_x(self):
        return self.__dimX

    def get_dim_y(self):
        return self.__dimY

    def get_file_path(self):
        return self.__filePath

    def get_output_file(self):
        return self.__outputFile

    def set_thickness(self, value):
        try:
            self.__thickness = float(value)
        except:
            self.__thickness = 0.0

    def set_dim_x(self, value):
        try:
            self.__dimX = float(value)
        except:
            self.__dimX = 0.0

    def set_dim_y(self, value):
        try:
            self.__dimY = float(value)
        except:
            self.__dimY = 0.0

    def set_file_path(self, value):
        self.__filePath = value
        self.__readFile()
        
    def set_output_file(self, value):
        self.__outputFile = value
        if self.isFile and value != None:
            myFileExtension = os.path.splitext(self.outputFile)[1];
            myCmbSheet = self.ima2cmb()
            if myFileExtension.upper() == ".SVG":
                myFileText = myCmbSheet.toSVG();
            elif myFileExtension.upper() == ".HTML" or myFileExtension.upper() == ".HTM":
                myFileText = myCmbSheet.toRaphael();
            elif myFileExtension.upper() == ".JS":
                myFileText = myCmbSheet.toJS();
            else:
                myFileText = str(myCmbSheet)
            myOut = open(value, "w")
            myOut.write(myFileText)
            myOut.close()

    def __clear(self):
        self.isFile = False
        self.programName = ""
        self.material = "0"
        self.thickness = 0.0
        self.formatCode = ""
        self.dimX = 0.0
        self.dimY = 0.0
        self.parts = []
        self.calls = []
        
    def __readFile(self):
        self.__clear()
        if self.filePath == None or not os.path.isfile(self.filePath):
            return
        try:
            mySection = Enum.ImaSection.none
            myFile = open(self.filePath, "r")
            for myLine in myFile:
                myLine = myLine.strip()
                myUpperLine = myLine.upper()
                isSection = len(myUpperLine) > 2 and myUpperLine.startswith("[") and myUpperLine.endswith("]")
                if isSection:
                    mySectionName = myUpperLine[1:-1]
                    if (mySection == Enum.ImaSection.none and mySectionName.startswith(Enum.ImaSection.general))\
                        or (mySection != Enum.ImaSection.none and mySectionName.startswith(Enum.ImaSection.calls))\
                        or (mySection != Enum.ImaSection.none and mySectionName.startswith(Enum.ImaSection.part))\
                        or (mySection == Enum.ImaSection.part and mySectionName.startswith(Enum.ImaSection.profile))\
                        or (mySection == Enum.ImaSection.profile and mySectionName.startswith(Enum.ImaSection.profile)):
                        mySection = mySectionName.split("_", 1)[0]
                        if mySection == Enum.ImaSection.part:
                            self.parts.append(Part())
                            self.parts[-1].index = len(self.parts)
                        elif mySection == Enum.ImaSection.profile:
                            self.parts[-1].profiles.append(Profile(myLine[1:-1]))
                            self.parts[-1].profiles[-1].index = len(self.parts[-1].profiles)
                else:
                    self.__parseLine(mySection, myLine)                    
        except IOError:
            self.__clear()
            
    def __parseLine(self, section, line):
        myKeyValue = line.split("=", 1)
        if len(myKeyValue) == 2:
            if (section == Enum.ImaSection.general):
                self.__parseLineGeneral(myKeyValue)
            elif (section == Enum.ImaSection.calls):
                self.__parseLineCalls(myKeyValue)
            elif (section == Enum.ImaSection.part):
                self.__parseLinePart(myKeyValue)
            elif (section == Enum.ImaSection.profile):
                self.__parseLineProfile(myKeyValue)
        return
        
    def __parseLineGeneral(self, keyValue):
        if not self.isFile:
            self.isFile = True
        myKey = keyValue[0].strip()
        myValue = keyValue[1].strip()
        for key, value in self._map.iteritems():
            if key.upper() == myKey.upper():
                setattr(self, value, myValue)
                break
        return
    
    def __parseLineCalls(self, keyValue):
        myKey = keyValue[0].strip()
        myValue = keyValue[1].strip()
        if myKey.upper().startswith("CALL_"):
            self.calls.append(Call(myKey, len(self.calls) + 1, myValue.split(",")))    
        return

    def __parseLinePart(self, keyValue):
        self.parts[-1].parseImaLine(keyValue)
        return

    def __parseLineProfile(self, keyValue):
        self.parts[-1].profiles[-1].parseImaLine(keyValue)
        return
    
    def ima2cmb(self):
        ret = None
        if self.isFile and len(self.parts) > 0 and len(self.calls) > 0:
            ret = sheet.Sheet(self.programName, self.dimX, self.dimY, self.thickness, self.isDebug)
            for myPart in self.parts:
                myIcon = Icon(myPart.name, 
                              myPart.dimX, 
                              myPart.dimY, 
                              myPart.pivotX, 
                              myPart.pivotY, 
                              myPart.massCenterX, 
                              myPart.massCenterY, 
                              myPart.area, 
                              myPart.isRawPart, 
                              myPart.isLabelPart)
                for myImaProfile in myPart.profiles:
                    myProfile = profile.Profile(myImaProfile.name, (myImaProfile.external != Enum.ExternalFlag.external), myIcon.dimX, myIcon.dimY, myIcon.pivotX, myIcon.pivotY)
                    for myItem in myImaProfile.items:
                        mySegment = segment.Segment(myItem.name, 
                                                    myItem.xStart, 
                                                    myItem.yStart, 
                                                    myItem.xEnd, 
                                                    myItem.yEnd)
                        if myItem.itemCode == Enum.ItemCode.counterClockwiseArc or myItem.itemCode == Enum.ItemCode.clockwiseArc:
                            mySegment.centerX = myItem.xCenter
                            mySegment.centerY = myItem.yCenter
                            mySegment.angle = myItem.angle
                            mySegment.isClockwise = (myItem.itemCode == Enum.ItemCode.clockwiseArc)
                            mySegment.radius = math.sqrt( (mySegment.centerX - mySegment.startX)**2 + (mySegment.centerY- mySegment.startY)**2 )
                        myProfile.segments.append(mySegment);
                    myIcon.profiles.append(myProfile)
                ret.icons.append(myIcon)
            index = 0
            for myCall in self.calls:
                index += 1
                myPosition = Position(myCall.name,
                                      index, 
                                      myCall.nestId, 
                                      ret.icons[myCall.partIndex - 1],
                                      myCall.xPos,
                                      myCall.yPos, 
                                      myCall.angle, 
                                      myCall.isSimmX, 
                                      myCall.isSimmY, 
                                      not myCall.isNotUnload,
                                      self.dimX, 
                                      self.dimY, 
                                      self.thickness)
                ret.positions.append(myPosition)
        return ret
    
    def __str__(self):
        myStr = "*** IMA FILE " + self.filePath + "\n"
        myStr += "FileExists: " + ("True" if self.isFile else "False") + "\n"
        myStr += "Program: " + self.programName + "\n"
        myStr += "Material: " + self.material + "\n"
        myStr += "Thickness: " + str(self.thickness) + "\n"
        myStr += "Format: " + self.formatCode + "\n"
        myStr += "X: " + str(self.dimX) + "\n"
        myStr += "Y: " + str(self.dimY) + "\n"
        myStr += "Parts: " + str(len(self.parts)) + "\n"
        for myPart in self.parts:
            myStr += "\n".join(("\t") + myLine for myLine in str(myPart).splitlines())        
            myStr += "\n"        
        myStr += "Calls: " + str(len(self.calls)) + "\n"
        for myCall in self.calls:
            myStr += "\n".join(("\t") + myLine for myLine in str(myCall).splitlines())        
            myStr += "\n"        
        return myStr
    
    filePath = property(get_file_path, set_file_path, None, None)
    outputFile = property(get_output_file, set_output_file, None, None)
    thickness = property(get_thickness, set_thickness, None, None)
    dimX = property(get_dim_x, set_dim_x, None, None)
    dimY = property(get_dim_y, set_dim_y, None, None)

if __name__ == '__main__':           # self test code
    myIma = Ima("/home/val3xiv/workspace-django/spr-sorting/sorting/media/myima/001_2010_3T5_X1_nest_lnt01.ima", "test.js", True)
    #myPart = myIma.parts[0].transform()
    myCmbSheet = myIma.ima2cmb()
    print myCmbSheet.toRaphael()
    #print myCmbSheet.toSVG()
    
        
        