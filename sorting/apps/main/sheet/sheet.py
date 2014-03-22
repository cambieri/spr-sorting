'''
Created on Nov 2, 2013

@author: val3xiv
'''
from main.ima._enum import Enum
from sorting.settings.common import SUCTION_CUPS

class Sheet(object):
    '''
    Element SHEET
    '''


    def __init__(self, code = "", dimX = 0.0, dimY = 0.0, dimZ = 0.0, isDebug = False):
        '''
        Constructor
        '''
        self.code = code
        self.dimX = dimX
        self.dimY = dimY
        self.dimZ = dimZ
        self.isDebug = isDebug
        self.icons = []
        self.positions = []


    def __str__(self):
        myStr = "SHEET " + self.code + " (" + str(self.dimX) + " x " + str(self.dimY) + " x " + str(self.dimZ) + ") " + str(len(self.icons)) + " icons, " + str(len(self.positions)) + " positions\n"
        for myElement in self.icons:
            myStr += "\n".join(("\t") + myLine for myLine in str(myElement).splitlines())        
            myStr += "\n"        
        for myElement in self.positions:
            myStr += "\n".join(("\t") + myLine for myLine in str(myElement).splitlines())        
            myStr += "\n"        
        return myStr
        
    def toSVG(self):
        ret = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
        ret += '<svg xmlns="http://www.w3.org/2000/svg"    height="' + str(self.dimY) + '" width="' + str(self.dimX) + '">\n'
        ret += '\t<rect x="0" y="0" height="' + str(self.dimY) + '" width="' + str(self.dimX) + '" style="fill:' + Enum.Colors.sheet + '" />\n'
        for myPosition in self.positions:
            ret += "\n".join(("\t\t") + myLine for myLine in myPosition.toSVGgroup().splitlines()) 
            ret += "\n"
        ret += '</svg>\n'
        return ret
    
    def toRaphael(self):
        ret = '<!DOCTYPE html> \n'
        ret += '<html> \n'
        ret += '\t<head> \n'
        ret += '\t\t<meta charset="utf-8"> \n'    
        ret += '\t\t<script src="js/raphael.js"></script> \n'
        ret += '\t\t<script src="js/jquery.js"></script> \n'
        ret += '\t\t<script src="js/cmbRaphael.js"></script> \n'
        ret += '\t\t<script> \n'
        ret += '\t\t\t$(document).ready(function(){ \n'
        ret += "\n".join(("\t\t\t\t") + myLine for myLine in self._jsFunction().splitlines()) 
        ret += "\n"
        ret += '\t\t\t}); \n'
        ret += '\t\t</script> \n'
        ret += '\t</head> \n'
        ret += '\t<body> \n'
        ret += '\t\t<div id="cmbR"></div> \n'
        ret += '\t</body> \n'
        ret += '</html> \n'
        return ret
    
    def toJS(self):
        ret = ""
        ret += "\n".join(myLine for myLine in self._jsFunction("drawSheet()").splitlines())         
        return ret
    
    def _jsFunction(self, functionName = None):
        ret = ""
        if (self.isDebug):
            ret += "var windowWidth = $('#cmbR').width() * 0.95; \n"
            ret += "var windowHeight = $('#cmbR').height() * 0.95; \n"
            ret += 'var xRatio = windowWidth / ' + str(self.dimX) + '; \n'
            ret += 'var yRatio = windowHeight / ' + str(self.dimY) + '; \n'
            ret += 'var ratio = (xRatio < yRatio) ? xRatio : yRatio; \n\n'
            ret += "var cmbR = Raphael('cmbR', " + str(self.dimX) + " * ratio, " + str(self.dimY) + " * ratio); \n"        
            ret += "cmbR.setViewBox(0,0,"+ str(self.dimX) + "," + str(self.dimY) + "); \n"
            ret += "cmbI = cmbR.set(); \n"
            ret += "cmbNotunload = cmbR.set(); \n"
            ret += "cmbPicked = cmbR.set(); \n"
            ret += "var r000 = cmbR.rect(0,0," + str(self.dimX) + "," + str(self.dimY) + "); \n"
            ret += 'r000.id = "r000"; \n' 
            ret += "$(r000.node).attr('class', 'sheet'); \n" 
            ret += "$(r000.node).attr('id', 'r000'); \n" 
            ret += "r000.attr({"
            ret += "'x': '" + "0" + "'"
            ret += ", 'y': '" + "0" + "'"
            ret += ", 'fill': '" + Enum.Colors.sheet + "'"
            ret += ", 'stroke': '" + "#000" + "'"
            ret += ", 'stroke-width': '" + "0" + "'"
            ret += ", 'stroke-opacity': '" + "1" + "'"
            ret += "}); \n\n"
        ret += "var cmbS = new Array(); \n"
        for mySuctionCup in SUCTION_CUPS:
            myScArray = '{"index":' + str(mySuctionCup[0])
            myScArray += ', "x":'  + str(mySuctionCup[1])
            myScArray += ', "y":'  + str(mySuctionCup[2])
            myScArray += ', "dimX":'  + str(mySuctionCup[3])
            myScArray += ', "dimY":'  + str(mySuctionCup[4])
            myScArray += ', "position":"'  + mySuctionCup[5] + '"}'
            ret += "cmbS.push(" + myScArray + "); \n"
        ret += "\n"                                    
        myTab = ""
        if (functionName != None):
            ret += "function " + functionName + " \n"
            ret += "{ \n"
            myTab = "\t"
        for myPosition in self.positions:
            ret += "\n".join((myTab) + myLine for myLine in myPosition.toRaphaelGroup().splitlines()) + "\n" 
        if (functionName != None):
            ret += "} \n"
        return ret
        
    
    
        