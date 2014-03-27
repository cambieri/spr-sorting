'''
Created on Sep 27, 2013

@author: val3xiv
'''
from bitarray import bitarray  # @UnresolvedImport
from enum import EnumLength
from enum import EnumResult

class TxMessage(object):
    '''
    Message for PLC
    '''
    protocol = { 'ic': (0, EnumLength.word)
                ,'function' : (16, EnumLength.word)
                ,'thickness' : (112, EnumLength.word)
                ,'plateausx' : (192, EnumLength.byte)
                ,'plateaudx' : (200, EnumLength.byte)
                ,'x' : (208, EnumLength.doubleWord)
                ,'y' : (240, EnumLength.doubleWord)
                ,'z' : (272, EnumLength.doubleWord)
                ,'a' : (304, EnumLength.doubleWord)
                ,'plateausx1' : (336, EnumLength.byte)
                ,'plateaudx1' : (344, EnumLength.byte)
                ,'x1' : (352, EnumLength.doubleWord)
                ,'y1' : (384, EnumLength.doubleWord)
                ,'z1' : (416, EnumLength.doubleWord)
                ,'a1' : (448, EnumLength.doubleWord)
                ,'ic1' : (512, EnumLength.word)
                ,'filler1' : (32, EnumLength.word)
                ,'filler3' : (128, EnumLength.word)
                ,'filler4' : (144, EnumLength.word)
                ,'filler5' : (160, EnumLength.word)
                ,'filler6' : (176, EnumLength.word)
                ,'filler7' : (480, EnumLength.word)
                ,'filler8' : (496, EnumLength.word)
                }
    for i in xrange(1, 9):
        for j in xrange(1, 9):
            protocol['sc' + str(j + (i-1) * 8)] = ((56 + (i - 1) * 8) - 1 - (j - 1), EnumLength.bit)
    messageBits = 528


    def __init__(self):
        '''
        Constructor
        ''' 
        self.reset()
    
    def reset(self):
        self.bits = bitarray(self.messageBits)
        self.bits.setall(False)        
        pass
    
    def numberToBits(self, num, length = EnumLength.byte):
        return bin(num)[2:].zfill(length)[-length:]
    
    def setValue(self, name, value):
        myName = name.lower().strip()
        if myName in self.protocol:
            index = self.protocol[myName][0]
            length = self.protocol[myName][1]
            myBits = bitarray(self.numberToBits(value, length))
            self.bits[index: index + length] = myBits
            return EnumResult.ok
        else:
            return EnumResult.dataUnexpected
            
if __name__ == '__main__':           # self test code
    myMessage = TxMessage()
    ret = EnumResult.ok
    ret = myMessage.setValue("IC",16) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("IC1",16) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("FUNCTION",201) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("SC6", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("SC7", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("SC11", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("SC24", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("SC26", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("SC30", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("PLATEAUSX", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("X", 80000) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("Y", 30000) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("PLATEAUSX1", 1) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("X1", 110000) if ret == EnumResult.ok else EnumResult.dataUnexpected
    ret = myMessage.setValue("Y1", 90000) if ret == EnumResult.ok else EnumResult.dataUnexpected
    print (ret == EnumResult.ok)
    print myMessage.bits if ret == EnumResult.ok else "error"
"""
    if (ret == EnumResult.ok):
        myStringToSend = myMessage.bits.tobytes();
        mySock = UdpClient()
        mySock.createsocket()
        print mySock.sendmessage(myStringToSend)
"""
                  

        