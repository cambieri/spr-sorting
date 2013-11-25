'''
Created on Nov 2, 2013

@author: val3xiv
'''
from _enum import Enum
from item import Item
class Profile(object):
    '''
    Element PROFILE
    '''


    def __init__(self, name = "", index = 0, tool = Enum.ToolType.unknown, external = Enum.ExternalFlag.unknown):
        '''
        Constructor
        '''
        self._map = {"Tool" : "tool",
                     "External" : "external"}
        self.name = name
        self.index = index
        self.tool = tool
        self.external = external
        self.items = []

    def get_index(self):
        return self.__index

    
    def get_tool(self):
        return self.__tool


    def get_external(self):
        return self.__external


    def set_index(self, value):
        try:
            self.__index = int(value)
        except:
            self.__index = 0
            
            
    def set_tool(self, value):
        try:
            self.__tool = int(value)
            isFound = False
            for key, value in Enum.ToolType.__dict__.iteritems():  # @UndefinedVariable
                if not key.startswith("_") and self.__tool == value:
                    isFound = True
                    break
            if not isFound:
                self.__tool = Enum.ToolType.unknown
        except:
            self.__tool = Enum.ToolType.unknown


    def set_external(self, value):
        try:
            self.__external = int(value)
            isFound = False
            for key, value in Enum.ExternalFlag.__dict__.iteritems():  # @UndefinedVariable
                if not key.startswith("_") and self.__external == value:
                    isFound = True
                    break
            if not isFound:
                self.__external = Enum.ExternalFlag.unknown
        except:
            self.__external = Enum.ExternalFlag.unknown
    
    def parseImaLine(self, keyValue):
        myKey = keyValue[0].strip()
        myValue = keyValue[1].strip()
        if myKey.upper().startswith("ITEM_"):
            self.items.append(Item(myKey, len(self.items) + 1, myValue.split(",")))
        else:
            for key, value in self._map.iteritems():
                if key.upper() == myKey.upper():
                    setattr(self, value, myValue)
                    break
        return        


    def __str__(self):
        myStr = ""
        myStr += "*** PROFILE " + self.name + "\n"
        myStr += "Index: " + str(self.index) + "\n"
        myStr += "Tool: "
        for key, value in Enum.ToolType.__dict__.iteritems():  # @UndefinedVariable
            if not key.startswith("_") and self.tool == value:
                myStr += key
                break
        myStr += "\n"
        myStr += "External: "
        for key, value in Enum.ExternalFlag.__dict__.iteritems():  # @UndefinedVariable
            if not key.startswith("_") and self.external == value:
                myStr += key
                break
        myStr += "\n"
        myStr += "Items: " + str(len(self.items)) + "\n"
        for myItem in self.items:
            myStr += "\n".join(("\t") + myLine for myLine in str(myItem).splitlines())
            myStr += "\n"        
        return myStr

    index = property(get_index, set_index, None, None)
    tool = property(get_tool, set_tool, None, None)
    external = property(get_external, set_external, None, None)
        
        
    