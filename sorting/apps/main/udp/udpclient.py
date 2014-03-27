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
import datetime
import time
class UdpClient(object):
    '''
    Simple socket client
    '''


    def __init__(self, host = None, port = None, lauchserver = True, objtools = None):
        '''
        Constructor
        '''
        self.thisname = "UDP Client"
        self.host = host if (host != None) else SOCKET_DATA['otherip']
        self.port = port if (port != None) else SOCKET_DATA['otherport']
        self.addr = (self.host, self.port)
        self.ic = random.randint(0, 32000)
        self.program = None
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0
        self.thickness = 0
        self.restart = False        
        self.tools = Tools() if objtools == None else objtools
        self.udpsocket = None
        if lauchserver:
            self.udpserver = UdpServer(SOCKET_DATA['myip'], SOCKET_DATA['myport'], SOCKET_DATA['bytesrx'], self.tools)
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
        
    def readfilepos(self):
        ret = False
        myFilePath = os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], SOCKET_DATA['file'])
        myPosFile = self.tools.readIniFile(myFilePath);
        if myPosFile:
            self.program = myPosFile.get("pack1.program")
            self.x = float(myPosFile.get("pack1.xpos"))
            self.y = float(myPosFile.get("pack1.ypos"))
            self.angle = float(myPosFile.get("pack1.angle"))
            self.restart = bool(int(myPosFile.get("pack1.restart")))
            os.rename(myFilePath, myFilePath + "." + str(datetime.datetime.now()).replace("-","").replace(" ", ".").replace(":",""))
            ret = True
        return ret 
    
    def readfilerequest(self):
        ret = False
        myFilePath = os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], SOCKET_DATA['filerequestsyn'])
        if (os.path.isfile(myFilePath)):
            myFilePath = os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], SOCKET_DATA['filerequest'])
            myRequestFile = self.tools.readIniFile(myFilePath);
            if myRequestFile:
                myReq = myRequestFile.get("main.code") if myRequestFile.get("main.code") != None else ""
                if myReq.lower().strip() == SOCKET_DATA['requesttext'].lower().strip():
                    try:
                        os.remove(os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], SOCKET_DATA['filerequestsyn']))
                    except Exception:
                        pass
                    try:
                        os.remove(os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], SOCKET_DATA['filerequest']))
                    except Exception:
                        pass
                    try:
                        responseFile = open(os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], SOCKET_DATA['fileresponse']), "w")
                        responseFile.write("[main]\r\n")
                        responseFile.write("code=WMS_C_PALLET_FOUND\r\n")
                    except Exception:
                        pass
                    finally:
                        try:
                            responseFile.close()
                        except Exception:
                            pass
                    try:
                        responseSyncFile = open(os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], SOCKET_DATA['fileresponsesyn']), "w")
                        responseSyncFile.write(" ")
                    except Exception:
                        pass
                    finally:
                        try:
                            responseSyncFile.close()
                        except Exception:                            
                            pass
                    myThicknessText = myRequestFile.get("main.zdim").strip() if myRequestFile.get("main.zdim") != None else ""
                    if (myThicknessText != ""):
                        try:
                            myThickness = int(float(myThicknessText) * SOCKET_DATA['thicknessfactor'])
                            if myThickness != self.thickness:
                                self.thickness = myThickness
                                ret = True
                        except Exception:
                            pass
        return ret 
        
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
    
    def sortingcommand(self, mission, isAskingState = False):
        myMessage = TxMessage()
        ret = EnumResult.ok
        if mission == None:
            myFunction = 202 if not isAskingState else 200
            ret = myMessage.setValue("FUNCTION", myFunction) if ret == EnumResult.ok else EnumResult.dataUnexpected
        else:
            mySCs = [myElement for myElement in mission.get("suctionCups") if myElement["on"] == 1]
            if len(mySCs) < 1:
                return EnumResult.dataUnexpected
            ret = myMessage.setValue("FUNCTION", 201) if ret == EnumResult.ok else EnumResult.dataUnexpected
            leftWing = mission.get("leftWing")
            rightWing = mission.get("rightWing")
            xLeaving = mission.get("offsetX") - leftWing
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
            if (leftWing > 0):
                ret = myMessage.setValue("PLATEAUSX", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
                ret = myMessage.setValue("PLATEAUSX1", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
            if (rightWing > 0):
                ret = myMessage.setValue("PLATEAUDX", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
                ret = myMessage.setValue("PLATEAUDX1", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected            
            for mySC in mySCs:
                ret = myMessage.setValue("SC" + str(mySC.get("index")), 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
        self.ic = self.ic + 1 if self.ic < 32000 else 1
        ret = myMessage.setValue("THICKNESS", self.thickness)
        ret = myMessage.setValue("IC", self.ic) if ret == EnumResult.ok else EnumResult.dataUnexpected
        ret = myMessage.setValue("IC1", self.ic) if ret == EnumResult.ok else EnumResult.dataUnexpected
        if (ret == EnumResult.ok):
            myStringToSend = myMessage.bits.tobytes();
            self.createsocket()
            myBytesSent = self.sendmessage(myStringToSend)
            mylog = []
            if myBytesSent != None:
                mylog.append(str(myBytesSent) + " byte(s) sent")
                mylog.append(list(bytearray(myStringToSend)))
                #print "\n[UDP Client] " + str(myBytesSent) + " byte(s) sent" 
                #print list(bytearray(myStringToSend))                
            else:
                mylog.append("ERROR")
                #print "\n[UDP Client] ERROR"
            self.tools.printLog(self.thisname, mylog)
        return ret
    
    def isFileWaiting(self):
        return os.path.isfile(os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], SOCKET_DATA['file'])) or os.path.isfile(os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], SOCKET_DATA['filerequestsyn']))
                                                                                                 
if __name__ == '__main__':           # self test code
    mytools = Tools()
    mysock = UdpClient(None, None, True, mytools)
    mysock.readfilerequest()
    mysock.sortingcommand(None, True)
    while 1:
        isFileRead = False
        while (not isFileRead):
            if mysock.readfilerequest():
                mysock.sortingcommand(None, True)
            isFileRead = mysock.readfilepos()
        isFirst = True
        mysock.udpserver.received = False
        time.sleep(5);
        while (not mysock.udpserver.received) and (not mysock.isFileWaiting()):
            pass
        if ((not mysock.restart) or (SOCKET_DATA['restartmanagement'] == 0)) and (not mysock.isFileWaiting()):        
            myMissions = mysock.readsorting()
            isLock = True
            if myMissions != None:
                for myMission in myMissions:
                    #isLock = False  #---VC DEBUG
                    isFile = mysock.isFileWaiting()
                    if mysock.isFileWaiting():
                        break;
                    while isLock:
                        if mysock.isFileWaiting():
                            break;
                        if isFirst:
                            myIcr = mysock.ic
                        else:
                            myIcr = mysock.udpserver.lastmessage.getValue('icr') if mysock.udpserver != None else None
                        myValue = mysock.udpserver.lastmessage.getValue('sortingwaiting') if mysock.udpserver != None else None
                        isLock = (myValue != 1 or myIcr != mysock.ic)
                    if not mysock.isFileWaiting():
                        if mysock.sortingcommand(myMission) == EnumResult.ok:
                            isFirst = False
                    isLock = True
        if not mysock.isFileWaiting():
            isLock = True
            while isLock:
                if mysock.isFileWaiting():
                    break
                if isFirst:
                    myIcr = mysock.ic
                else:
                    myIcr = mysock.udpserver.lastmessage.getValue('icr') if mysock.udpserver != None else None
                myValue = mysock.udpserver.lastmessage.getValue('sortingwaiting') if mysock.udpserver != None else None
                isLock = (myValue != 1 or myIcr != mysock.ic)
                if (not isLock):             
                    mysock.sortingcommand(None)
    
        
        
