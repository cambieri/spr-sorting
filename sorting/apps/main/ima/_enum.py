'''
Created on Nov 1, 2013

@author: val3xiv
'''

class Enum:
    
    class ItemCode:
        unknown = 0
        line = 1
        clockwiseArc = 2
        counterClockwiseArc = 3
        
    class ToolType:
        unknown = 0
        cut = 1
        mark = 2
        
    class ExternalFlag:
        unknown = -1
        internal = 0
        external = 1
        
    class ImaSection:
        none = ""
        general = "GENERAL"
        calls = "CALLS"
        part = "PART"
        profile = "PROFILE"
        
    class Colors:
        sheet = "#F7FE2E"
        external = "#585858"
        internal = "#F7FE2E"
        notunload = "#B40431"         
    

        
        