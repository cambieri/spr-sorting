'''
Created on Nov 1, 2013

@author: val3xiv
'''

from _enum import Enum
class Item(object):
    '''
    Element ITEM
    '''


    def __init__(self, name = "", index = 0, paramList = []):
        '''
        Constructor
        '''
        self.name = name
        self.index = index
        self.itemCode = Enum.ItemCode.unknown
        self.xStart = 0.0
        self.yStart = 0.0
        self.xEnd = 0.0
        self.yEnd = 0.0
        self.xCenter = 0.0
        self.yCenter = 0.0
        self.angle = 0.0
                
        props = {0 : "itemCode",
                 1 : "xStart",
                 2 : "yStart",
                 3 : "xEnd",
                 4 : "yEnd",
                 5 : "xCenter",
                 6 : "yCenter",
                 7 : "angle"
        }
        for index, value in props.iteritems():
            if len(paramList) >= index + 1:
                setattr(self, value, paramList[index])

    def get_index(self):
        return self.__index

    
    def get_item_code(self):
        return self.__itemCode


    def get_x_start(self):
        return self.__xStart


    def get_y_start(self):
        return self.__yStart


    def get_x_end(self):
        return self.__xEnd


    def get_y_end(self):
        return self.__yEnd


    def get_x_center(self):
        return self.__xCenter


    def get_y_center(self):
        return self.__yCenter


    def get_angle(self):
        return self.__angle


    def set_index(self, value):
        try:
            self.__index = int(value)
        except:
            self.__index = 0

    def set_item_code(self, value):
        try:
            self.__itemCode = int(value)
            isFound = False
            for key, value in Enum.ItemCode.__dict__.iteritems():  # @UndefinedVariable
                if not key.startswith("_") and self.__itemCode == value:
                    isFound = True
                    break
            if not isFound:
                self.__itemCode = Enum.ItemCode.unknown
        except:
            self.__itemCode = Enum.ItemCode.unknown


    def set_x_start(self, value):
        try:
            self.__xStart = float(value)
        except:
            self.__xStart = 0.0


    def set_y_start(self, value):
        try:
            self.__yStart = float(value)
        except:
            self.__yStart = 0.0


    def set_x_end(self, value):
        try:
            self.__xEnd = float(value)
        except:
            self.__xEnd = 0.0


    def set_y_end(self, value):
        try:
            self.__yEnd = float(value)
        except:
            self.__yEnd = 0.0


    def set_x_center(self, value):
        try:
            self.__xCenter = float(value)
        except:
            self.__xCenter = 0.0

    def set_y_center(self, value):
        try:
            self.__yCenter = float(value)
        except:
            self.__yCenter = 0.0


    def set_angle(self, value):
        try:
            self.__angle = float(value)
        except:
            self.__angle = 0.0
    
        
    def __str__(self):
        myStr = ""
        myStr += "*** ITEM " + self.name + "\n"
        myStr += "Index: " + str(self.index) + "\n" 
        myStr += "Code: "
        for key, value in Enum.ItemCode.__dict__.iteritems():  # @UndefinedVariable
            if not key.startswith("_") and self.itemCode == value:
                myStr += key
                break
        myStr += "\n"
        myStr += "Xstart: " + str(self.xStart) + "\n" 
        myStr += "Ystart: " + str(self.yStart) + "\n"
        myStr += "Xend: " + str(self.xEnd) + "\n"
        myStr += "Yend: " + str(self.yEnd) + "\n"
        if self.itemCode == Enum.ItemCode.counterClockwiseArc or self.itemCode == Enum.ItemCode.clockwiseArc:
            myStr += "Xcenter: " + str(self.xCenter) + "\n" 
            myStr += "Ycenter: " + str(self.yCenter) + "\n"
            myStr += "Angle: " + str(self.angle) + "\n"
        return myStr
    
    index = property(get_index, set_index, None, None)
    itemCode = property(get_item_code, set_item_code, None, None)
    xStart = property(get_x_start, set_x_start, None, None)
    yStart = property(get_y_start, set_y_start, None, None)
    xEnd = property(get_x_end, set_x_end, None, None)
    yEnd = property(get_y_end, set_y_end, None, None)
    xCenter = property(get_x_center, set_x_center, None, None)
    yCenter = property(get_y_center, set_y_center, None, None)
    angle = property(get_angle, set_angle, None, None)
                
                    
if __name__ == '__main__':           # self test code
    myItem = Item(paramList=[3, 14, 20, 25, 20, 10, 10, 130])


        