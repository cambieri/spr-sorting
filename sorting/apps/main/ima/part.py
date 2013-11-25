'''
Created on Nov 2, 2013

@author: val3xiv
'''
from _enum import Enum
from profile import Profile
import copy
import math
class Part(object):
    '''
    Element PART
    '''

    def __init__(self, 
                 name = "", index = 0,
                 dimX = 0.0, dimY = 0.0, 
                 pivotX = 0.0, pivotY = 0.0, 
                 massCenterX = 0.0, massCenterY = 0.0, 
                 area = 0.0, isRawPart = False, isLabelPart = False):
        '''
        Constructor
        '''
        self._map = {"PartName" : "name",
                     "DimX" : "dimX",
                     "DimY" : "dimY",
                     "PivotX" : "pivotX",
                     "PivotY" : "pivotY",
                     "MassCenterX" : "massCenterX",
                     "MassCenterY" : "massCenterY",
                     "Area" : "area",
                     "RawPart" : "isRawPart",
                     "LabelPart" : "isLabelPart"}
        self.name = name
        self.index = index
        self.dimX = dimX
        self.dimY = dimY
        self.pivotX = pivotX
        self.pivotY = pivotY
        self.massCenterX = massCenterX
        self.massCenterY = massCenterY
        self.area = area
        self.isRawPart = isRawPart
        self.isLabelPart = isLabelPart
        self.profiles = []

    def get_is_label_part(self):
        return self.__isLabelPart


    def get_is_raw_part(self):
        return self.__isRawPart


    def get_index(self):
        return self.__index

    
    def get_dim_x(self):
        return self.__dimX


    def get_dim_y(self):
        return self.__dimY


    def get_pivot_x(self):
        return self.__pivotX


    def get_pivot_y(self):
        return self.__pivotY


    def get_mass_center_x(self):
        return self.__massCenterX


    def get_mass_center_y(self):
        return self.__massCenterY


    def get_area(self):
        return self.__area


    def set_is_raw_part(self, value):
        try:
            self.__isRawPart = bool(int(value))
        except:
            self.__isRawPart = False


    def set_is_label_part(self, value):
        try:
            self.__isLabelPart = bool(int(value))
        except:
            self.__isLabelPart = False


    def set_index(self, value):
        try:
            self.__index = int(value)
        except:
            self.__index = 0

    
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


    def set_pivot_x(self, value):
        try:
            self.__pivotX = float(value)
        except:
            self.__pivotX = 0.0


    def set_pivot_y(self, value):
        try:
            self.__pivotY = float(value)
        except:
            self.__pivotY = 0.0


    def set_mass_center_x(self, value):
        try:
            self.__massCenterX = float(value)
        except:
            self.__massCenterX = 0.0


    def set_mass_center_y(self, value):
        try:
            self.__massCenterY = float(value)
        except:
            self.__massCenterY = 0.0


    def set_area(self, value):
        try:
            self.__area = float(value)
        except:
            self.__area = 0.0


    def parseImaLine(self, keyValue):
        myKey = keyValue[0].strip()
        myValue = keyValue[1].strip()
        for key, value in self._map.iteritems():
            if key.upper() == myKey.upper():
                setattr(self, value, myValue)
                break
        return
    
    def transform(self, x = None, y = None, angle = 0.0, isSimmX = False, isSimmY = False):
        myPart = copy.deepcopy(self)
        if x == None:
            x = myPart.pivotX
        if y == None:
            y = myPart.pivotY
        deltaX = x - myPart.pivotX
        deltaY = y - myPart.pivotY
        if isSimmX and isSimmY:
            angle += 180
        radAngle = angle * math.pi / 180
        for myProfile in myPart.profiles:
            for myItem in myProfile.items:
                if radAngle != 0:
                    myItem.xStart = math.cos(radAngle) * (myItem.xStart - myPart.pivotX) - math.sin(radAngle) * (myItem.yStart - myPart.pivotY) + myPart.pivotX
                    myItem.yStart = math.sin(radAngle) * (myItem.xStart - myPart.pivotX) + math.cos(radAngle) * (myItem.yStart - myPart.pivotY) + myPart.pivotY
                    myItem.xEnd = math.cos(radAngle) * (myItem.xEnd - myPart.pivotX) - math.sin(radAngle) * (myItem.yEnd - myPart.pivotY) + myPart.pivotX
                    myItem.yEnd = math.sin(radAngle) * (myItem.xEnd - myPart.pivotX) + math.cos(radAngle) * (myItem.yEnd - myPart.pivotX) + myPart.pivotY
                    if myItem.itemCode == Enum.ItemCode.clockwiseArc or myItem.itemCode == Enum.ItemCode.counterClockwiseArc:
                        myItem.xCenter = math.cos(radAngle) * (myItem.xCenter - myPart.pivotX) - math.sin(radAngle) * (myItem.yCenter - myPart.pivotY) + myPart.pivotX
                        myItem.yCenter = math.sin(radAngle) * (myItem.xCenter - myPart.pivotX) + math.cos(radAngle) * (myItem.yCenter - myPart.pivotY) + myPart.pivotY
                if isSimmX and not isSimmY:
                    myItem.yStart = 2 * myPart.pivotY - myItem.yStart 
                    myItem.yEnd = 2 * myPart.pivotY - myItem.yEnd
                    if myItem.itemCode == Enum.ItemCode.clockwiseArc or myItem.itemCode == Enum.ItemCode.counterClockwiseArc:
                        myItem.yCenter = 2 * myPart.pivotY - myItem.yCenter
                        if myItem.itemCode == Enum.ItemCode.clockwiseArc:
                            myItem.itemCode = Enum.ItemCode.counterClockwiseArc
                        else:
                            myItem.itemCode = Enum.ItemCode.clockwiseArc
                elif isSimmY and not isSimmX:
                    myItem.xStart = 2 * myPart.pivotX - myItem.cStart 
                    myItem.xEnd = 2 * myPart.pivotX - myItem.xEnd
                    if myItem.itemCode == Enum.ItemCode.clockwiseArc or myItem.itemCode == Enum.ItemCode.counterClockwiseArc:
                        myItem.xCenter = 2 * myPart.pivotX - myItem.xCenter
                        if myItem.itemCode == Enum.ItemCode.clockwiseArc:
                            myItem.itemCode = Enum.ItemCode.counterClockwiseArc
                        else:
                            myItem.itemCode = Enum.ItemCode.clockwiseArc
                myItem.xStart += deltaX
                myItem.yStart += deltaY
                myItem.xEnd += deltaX
                myItem.yEnd += deltaY
                if myItem.itemCode == Enum.ItemCode.clockwiseArc or myItem.itemCode == Enum.ItemCode.counterClockwiseArc:
                    myItem.xCenter += deltaX
                    myItem.yCenter += deltaY
        myPart.pivotX += deltaX
        myPart.pivotY += deltaY               
        return myPart
        
    def __countProfiles(self, isExternal = True):
        myCount = 0
        myProfile = Profile()
        for myProfile in self.profiles:
            if isExternal == None: 
                myCount += 1
            elif isExternal and myProfile.external == Enum.ExternalFlag.external:
                myCount +=1
            elif (not isExternal) and (myProfile.external == Enum.ExternalFlag.internal):
                myCount +=1
        return myCount
    
    def countAllProfiles(self): return self.__countProfiles(None)
    def countExternalProfiles(self): return self.__countProfiles(True)
    def countInternalProfiles(self): return self.__countProfiles(False)

    def __str__(self):
        myStr = ""
        myStr += "*** PART " + self.name + "\n"
        myStr += "Index: " + str(self.index)+ "\n"
        myStr += "DimX: " + str(self.dimX)+ "\n"
        myStr += "DimY: " + str(self.dimY)+ "\n"
        myStr += "PivotX: " + str(self.pivotX)+ "\n"
        myStr += "PivotY: " + str(self.pivotY)+ "\n"
        myStr += "MassCenterX: " + str(self.massCenterX)+ "\n"
        myStr += "MassCenterY: " + str(self.massCenterY)+ "\n"
        myStr += "Area: " + str(self.area)+ "\n"
        myStr += "RawPart: " + ("True" if self.isRawPart else "False") + "\n"
        myStr += "LabelPart: " + ("True" if self.isLabelPart else "False") + "\n"
        myStr += "Profiles: {0:d} external, {1:d} internal, {2:d} total\n".format(self.countExternalProfiles(), self.countInternalProfiles(), self.countAllProfiles())
        for myProfile in self.profiles:
            myStr += "\n".join(("\t") + myLine for myLine in str(myProfile).splitlines())        
            myStr += "\n"        
        return myStr
    
    index = property(get_index, set_index, None, None)
    dimX = property(get_dim_x, set_dim_x, None, None)
    dimY = property(get_dim_y, set_dim_y, None, None)
    pivotX = property(get_pivot_x, set_pivot_x, None, None)
    pivotY = property(get_pivot_y, set_pivot_y, None, None)
    massCenterX = property(get_mass_center_x, set_mass_center_x, None, None)
    massCenterY = property(get_mass_center_y, set_mass_center_y, None, None)
    area = property(get_area, set_area, None, None)
    isRawPart = property(get_is_raw_part, set_is_raw_part, None, None)
    isLabelPart = property(get_is_label_part, set_is_label_part, None, None)
    
    