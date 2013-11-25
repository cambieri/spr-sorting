'''
Created on Nov 2, 2013

@author: val3xiv
'''

class Call(object):
    '''
    Element CALL
    '''


    def __init__(self, name = "", index = 0, paramList = []):
        '''
        Constructor
        '''
        self.name = name
        self.index = index
        self.partIndex = 0
        self.xPos = 0.0
        self.yPos = 0.0
        self.angle = 0.0
        self.isSimmX = False
        self.isSimmY = False
        self.type = "0"
        self.nestId = "0"
        self.isNotUnload = False
        self.linkedPartIndex = 0
        props = {0 : "partIndex",
                 1 : "xPos",
                 2 : "yPos",
                 3 : "angle",
                 4 : "isSimmX",
                 5 : "isSimmY",
                 6 : "type",
                 7 : "nestId",
                 8 : "isNotUnload",
                 9 : "linkedPartIndex"
        }
        for index, value in props.iteritems():
            if len(paramList) >= index + 1:
                setattr(self, value, paramList[index])


    def get_index(self):
        return self.__index

    
    def get_is_simm_x(self):
        return self.__isSimmX


    def get_is_simm_y(self):
        return self.__isSimmY


    def get_is_not_unload(self):
        return self.__isNotUnload


    def set_index(self, value):
        try:
            self.__index = int(value)
        except:
            self.__index = 0

    
    def set_is_simm_x(self, value):
        try:
            self.__isSimmX = bool(int(value))
        except:
            self.__isSimmX = False


    def set_is_simm_y(self, value):
        try:
            self.__isSimmY = bool(int(value))
        except:
            self.__isSimmY = False


    def set_is_not_unload(self, value):
        try:
            self.__isNotUnload = bool(int(value))
        except:
            self.__isNotUnload = False


    def get_part_index(self):
        return self.__partIndex


    def get_x_pos(self):
        return self.__xPos


    def get_y_pos(self):
        return self.__yPos


    def get_angle(self):
        return self.__angle


    def get_linked_part_index(self):
        return self.__linkedPartIndex


    def set_part_index(self, value):
        try:
            self.__partIndex = int(value)
        except:
            self.__partIndex = 0
            

    def set_x_pos(self, value):
        try:
            self.__xPos = float(value)
        except:
            self.__xPos = 0.0

    def set_y_pos(self, value):
        try:
            self.__yPos = float(value)
        except:
            self.__yPos = 0.0

    def set_angle(self, value):
        try:
            self.__angle = float(value)
        except:
            self.__angle = 0.0

    def set_linked_part_index(self, value):
        try:
            self.__linkedPartIndex = int(value)
        except:
            self.__linkedPartIndex = 0

    def __str__(self):
        myStr = ""
        myStr += "*** CALL " + self.name + "\n"
        myStr += "Index: " + str(self.index) + "\n"
        myStr += "PartIndex: " + str(self.partIndex) + "\n"
        myStr += "Xpos: " + str(self.xPos) + "\n"
        myStr += "Ypos: " + str(self.yPos) + "\n"
        myStr += "Angle: " + str(self.angle) + "\n"
        myStr += "Xsimmetry: " + ("True" if self.isSimmX else "False") + "\n"
        myStr += "Ysimmetry: " + ("True" if self.isSimmY else "False") + "\n"
        myStr += "Type: " + self.type + "\n"
        myStr += "NestId: " + self.nestId + "\n"
        myStr += "NotUnload: " + ("True" if self.isNotUnload else "False") + "\n"
        myStr += "LinkedPartIndex: " + str(self.linkedPartIndex) + "\n"        
        return myStr
    
    index = property(get_index, set_index, None, None)
    partIndex = property(get_part_index, set_part_index, None, None)
    xPos = property(get_x_pos, set_x_pos, None, None)
    yPos = property(get_y_pos, set_y_pos, None, None)
    angle = property(get_angle, set_angle, None, None)
    linkedPartIndex = property(get_linked_part_index, set_linked_part_index, None, None)
    isSimmX = property(get_is_simm_x, set_is_simm_x, None, None)
    isSimmY = property(get_is_simm_y, set_is_simm_y, None, None)
    isNotUnload = property(get_is_not_unload, set_is_not_unload, None, None)
                
                
                
        