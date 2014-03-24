'''
Created on Sep 27, 2013

@author: val3xiv
'''

import socket
from sorting.settings.common import SOCKET_DATA
from sorting.settings.common import MEDIA_ROOT
import os
from main.tools import Tools;
from enum import EnumResult
from txmessage import TxMessage
from udpserver import UdpServer
import json
import math
import random
import time
class UdpClient(object):
    '''
    Simple socket client
    '''


    def __init__(self, host = None, port = None, lauchserver = True):
        '''
        Constructor
        '''
        self.host = host if (host != None) else SOCKET_DATA['otherip']
        self.port = port if (port != None) else SOCKET_DATA['otherport']
        self.addr = (self.host, self.port)
        self.ic = random.randint(0, 32000)
        self.program = None
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0
        self.restart = False
        self.tools = Tools()
        self.udpsocket = None
        if lauchserver:
            self.udpserver = UdpServer(SOCKET_DATA['myip'], SOCKET_DATA['myport'], SOCKET_DATA['bytesrx'])
            self.udpserver.start()
        
    def createsocket(self):
        if self.udpsocket == None:
            self.udpsocket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        
    def sendmessage(self, data):
        ret = None
        if not data:
            pass
        else:
            try:
                ret = self.udpsocket.sendto(data, self.addr)
            except Exception:
                ret = None
        return ret
    
    def closesocket(self):
        if self.udpsocket:
            self.udpsocket.close()
            self.udpsocket = None
        
    def readfile(self):
        myFilePath = os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], SOCKET_DATA['file'])
        myPosFile = self.tools.readIniFile(myFilePath);
        if myPosFile:
            self.program = myPosFile.get("pack1.program")
            self.x = float(myPosFile.get("pack1.xpos"))
            self.y = float(myPosFile.get("pack1.ypos"))
            self.angle = float(myPosFile.get("pack1.angle"))
            self.restart = bool(int(myPosFile.get("pack1.restart"))) 
    
    def readsorting(self):
        ret = []
        myFilePath = os.path.join(MEDIA_ROOT, 'sorting', self.program.strip() + ".sor")
        if os.path.isfile(myFilePath):
            with open(myFilePath) as myFile:
                for myLine in myFile:
                    myJsonLine = json.loads(myLine)
                    for myJsonElement in myJsonLine:
                        ret.append(myJsonElement)            
        return ret if len(ret) > 0 else None   
    
    def sortingstate(self):
        myMessage = TxMessage()
        ret = EnumResult.ok
        ret = myMessage.setValue("FUNCTION", 200) if ret == EnumResult.ok else EnumResult.dataUnexpected
        self.ic = self.ic + 1 if self.ic < 32000 else 1
        ret = myMessage.setValue("IC", self.ic) if ret == EnumResult.ok else EnumResult.dataUnexpected
        ret = myMessage.setValue("IC1", self.ic) if ret == EnumResult.ok else EnumResult.dataUnexpected
        if (ret == EnumResult.ok):
            myStringToSend = myMessage.bits.tobytes();
            self.createsocket()
            myBytesSent = self.sendmessage(myStringToSend)
            if myBytesSent != None:
                print "\n[UDP Client] " + str(myBytesSent) + " byte(s) sent" 
                print list(bytearray(myStringToSend))                
            else:
                print "\n[UDP Client] ERROR"
        return ret
    
    def sortingcommand(self, mission, isAskingState = False):
        myMessage = TxMessage()
        ret = EnumResult.ok
        if mission == None:
            myFunction = 202 if not isAskingState else 200
            ret = myMessage.setValue("FUNCTION", myFunction) if ret == EnumResult.ok else EnumResult.dataUnexpected
        else:
            ret = myMessage.setValue("FUNCTION", 201) if ret == EnumResult.ok else EnumResult.dataUnexpected
            xLeaving = mission.get("offsetX")
            yLeaving = mission.get('offsetY')
            xTaking = xLeaving + self.x
            yTaking = yLeaving + self.y
            (xTaking, yTaking) = self.tools.rotatePoint((xTaking, yTaking), self.angle)
            xLeaving = int(math.ceil(xLeaving *  SOCKET_DATA["dimensionfactor"]))
            yLeaving = int(math.ceil(yLeaving *  SOCKET_DATA["dimensionfactor"]))
            xTaking = int(math.ceil(xTaking *  SOCKET_DATA["dimensionfactor"]))
            yTaking = int(math.ceil(yTaking *  SOCKET_DATA["dimensionfactor"]))
            ret = myMessage.setValue("X", xTaking) if ret == EnumResult.ok else EnumResult.dataUnexpected
            ret = myMessage.setValue("Y", yTaking) if ret == EnumResult.ok else EnumResult.dataUnexpected
            ret = myMessage.setValue("X1", xLeaving) if ret == EnumResult.ok else EnumResult.dataUnexpected
            ret = myMessage.setValue("Y1", yLeaving) if ret == EnumResult.ok else EnumResult.dataUnexpected
            if (mission.get("leftWing")):
                ret = myMessage.setValue("PLATEAUSX", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
                ret = myMessage.setValue("PLATEAUSX1", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
            if (mission.get("rightWing")):
                ret = myMessage.setValue("PLATEAUDX", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
                ret = myMessage.setValue("PLATEAUDX1", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected            
            mySCs = [myElement for myElement in mission.get("suctionCups") if myElement["color"].upper() == "#00FF00"]
            for mySC in mySCs:
                ret = myMessage.setValue("SC" + str(mySC.get("index")), 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
        self.ic = self.ic + 1 if self.ic < 32000 else 1
        ret = myMessage.setValue("IC", self.ic) if ret == EnumResult.ok else EnumResult.dataUnexpected
        ret = myMessage.setValue("IC1", self.ic) if ret == EnumResult.ok else EnumResult.dataUnexpected
        if (ret == EnumResult.ok):
            myStringToSend = myMessage.bits.tobytes();
            self.createsocket()
            myBytesSent = self.sendmessage(myStringToSend)
            if myBytesSent != None:
                print "\n[UDP Client] " + str(myBytesSent) + " byte(s) sent" 
                print list(bytearray(myStringToSend))                
            else:
                print "\n[UDP Client] ERROR"
        return ret
                                                                                                 
if __name__ == '__main__':           # self test code
    mysock = UdpClient()
    #mysock.sortingstate()
    mysock.sortingcommand(None, True)
    mysock.readfile()
    isFirst = True
    if not mysock.restart:        
        myMissions = mysock.readsorting()
        isLock = True
        for myMission in myMissions:
            #isLock = False  #---VC DEBUG
            while isLock:
                if isFirst:
                    myIcr = mysock.ic
                else:
                    myIcr = mysock.udpserver.lastmessage.getValue('icr') if mysock.udpserver != None else None
                myValue = mysock.udpserver.lastmessage.getValue('sortingwaiting') if mysock.udpserver != None else None
                isLock = (myValue != 1 or myIcr != mysock.ic) 
            mysock.sortingcommand(myMission)
            isFirst = False
            isLock = True
    while isLock:
        if isFirst:
            myIcr = mysock.ic
        else:
            myIcr = mysock.udpserver.lastmessage.getValue('icr') if mysock.udpserver != None else None
        myValue = mysock.udpserver.lastmessage.getValue('sortingwaiting') if mysock.udpserver != None else None
        isLock = (myValue != 1 or myIcr != mysock.ic) 
    mysock.sortingcommand(None)
        
        
