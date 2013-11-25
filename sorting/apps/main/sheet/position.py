'''
Created on Nov 8, 2013

@author: val3xiv
'''
from main.ima._enum import Enum

class Position(object):
    '''
    Element POSITION
    '''


    def __init__(self, 
                 code = "", index = -1, idPosition = "", icon = None,
                 positionX = None, positionY = None, angle = 0,
                 isSimmetryX = False, isSimmetryY = False,
                 isToUnload = True,
                 sheetX = 0, sheetY = 0, sheetZ = 0):
        '''
        Constructor
        '''
        self.code = code
        self.index = index
        self.idPosition = idPosition
        self.icon = icon
        self.positionX = positionX
        self.positionY = positionY
        self.angle = angle
        self.isSimmetryX = isSimmetryX
        self.isSimmetryY = isSimmetryY
        self.isToUnload = isToUnload
        self.sheetX = sheetX
        self.sheetY = sheetY
        self.sheetZ = sheetZ

    def __str__(self):        
        myStr = "POSITION " + str(self.index) + ") " + self.code 
        myStr += " (icon: " + str(self.icon.code) 
        if (self.positionX != None and self.positionY != None):
            myStr += ", position: " + str(self.positionX) + ", " + str(self.positionY)
        if self.angle != 0:
            myStr += ", angle: " + str(self.angle)
        myStr += ", simmetryX" if self.isSimmetryX else ""
        myStr += ", simmetryY" if self.isSimmetryY else ""
        myStr += "" if self.isToUnload else ", not-unload"
        myStr += ", sheet: " + str(self.sheetY) + " x " + str(self.sheetY) + " x " + str(self.sheetZ)
        myStr += ")\n"
        return myStr
    
    def toSVGgroup (self):
        diffX = self.positionX - self.icon.pivotX
        diffY = self.positionY - self.icon.pivotY
        transform = 'transform="translate(0,' + str(self.sheetY) + ') scale(1, -1)'
        transform += ' translate(' + str(diffX) + ', ' + str(diffY) + ') '
        transform += '' if self.angle == 0 else (' rotate(' + str(self.angle) + ',' + str(self.icon.pivotX) + ',' + str(self.icon.pivotY) + ') ')
        if self.isSimmetryX or self.isSimmetryY:
            transform +=  ' scale(' + ('-1' if self.isSimmetryX else '1') + ',' + ('-1' if self.isSimmetryY else '1') + ')' 
        transform += '"'
        ret = '<g id="' + str(self.index) + '-' + self.icon.code + '" class="' + ('default' if self.isToUnload else 'not-unload') + '">\n'
        myProfileIndex = 0
        for myProfile in self.icon.profiles:
            myProfileIndex +=1
            myId = str(self.index) + "-" + str(myProfileIndex) + "-" + myProfile.code 
            if myProfile.isInternal:
                myClass = "internal"
                myColor = Enum.Colors.internal
            else:
                myClass = "external"
                myColor = Enum.Colors.external if self.isToUnload else Enum.Colors.notunload
            ret += '\t<path id="' + myId + '" class="' + myClass + '" \n'
            ret += "\n".join(("\t\t") + myLine for myLine in myProfile.toSVGpath().splitlines())        
            ret += "\n"                    
            ret += '\t\tstyle="fill:' + myColor + ';"\n'
            ret += '\t\t' + transform +' \n'
            ret += '\t/>\n'
        ret += '</g>\n'
        return ret

    def toRaphaelGroup (self):
        diffX = self.positionX - self.icon.pivotX
        diffY = self.positionY - self.icon.pivotY
        transform = 't0,' + str(self.sheetY) + ' s1,-1'
        transform += ' t' + str(diffX) + ',' + str(diffY)
        transform += '' if self.angle == 0 else (' r' + str(self.angle) + ',' + str(self.icon.pivotX) + ',' + str(self.icon.pivotY))
        if self.isSimmetryX or self.isSimmetryY:
            transform +=  ' s' + ('-1' if self.isSimmetryX else '1') + ',' + ('-1' if self.isSimmetryY else '1') 
        myGroupName = 'g' + str(self.index).zfill(3)
        ret = 'var ' + myGroupName + ' = cmbR.set(); \n'
        ret += myGroupName + '.id = "' + myGroupName + '"; \n';
        myProfileIndex = 0
        for myProfile in self.icon.profiles:
            myProfileIndex +=1
            myId = "p" + str(self.index).zfill(3) + str(myProfileIndex).zfill(3) 
            if myProfile.isInternal:
                myClass = "internal"
                myColor = Enum.Colors.internal
            else:
                myClass = "external"
                myColor = Enum.Colors.external if self.isToUnload else Enum.Colors.notunload
            ret += 'pathString = "' + myProfile.toRaphaelPath() + '"; \n'
            ret += 'pathTransform = "' + transform + '"; \n'
            ret += 'pathArray = Raphael.transformPath(pathString, pathTransform); \n'
            ret += 'pathToString = pathArrayToString(pathArray); \n'
            ret += 'var ' + myId + ' = cmbR.path(pathArray); \n'
            ret += myId + '.id = "' + myId + '"; \n';
            ret += "$(" + myId + ".node).attr('class', '" + myClass + "'); \n";
            ret += "$(" + myId + ".node).attr('id', '" + myId + "'); \n";
            ret += myId + ".attr({"
            ret += "'fill': '" + myColor + "'"
            ret += ", 'stroke': '" + "#000" + "'"
            ret += ", 'stroke-width': '" + "0" + "'"
            ret += ", 'stroke-opacity': '" + "1" + "'"
            ret += "}); \n"
            ret += myId + '.data("id", "' + myId + '"); \n'
            ret += myId + '.data("class", "' + myClass + '"); \n'
            ret += myId + '.data("picked", 0); \n'
            ret += myId + '.data("notunload", ' + ('0' if self.isToUnload else '1') + '); \n';
            ret += myId + '.data("parent", ' + myGroupName + '); \n'
            ret += myId + '.data("pathstring", pathToString); \n'
            ret += myGroupName + ".push(" + myId + "); \n"
        ret += "cmbI.push(" + myGroupName + "); \n"
        if not self.isToUnload:
            ret += 'cmbNotunload.push("' + myGroupName + '"); \n"'
        ret += '\n'
        return ret
        