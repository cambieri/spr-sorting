'''
Created on Mar 21, 2014

@author: val3xiv
'''
from bitarray import bitarray  # @UnresolvedImport
from enum import EnumLength

class RxMessage(object):
    '''
    Message from PLC
    '''
    protocol = { 'icr': (0, EnumLength.word)
                ,'errorack' : (16, EnumLength.byte)
                ,'acknack' : (24, EnumLength.byte)
                ,'sortingerror' : (45, EnumLength.bit)
                ,'sortingrunning' : (46, EnumLength.bit)
                ,'sortingwaiting' : (47, EnumLength.bit)
                ,'sortingfunction' : (48, EnumLength.word)
                ,'z1error' : (77, EnumLength.bit)
                ,'z1running' : (78, EnumLength.bit)
                ,'z1waiting' : (79, EnumLength.bit)
                ,'z1function' : (80, EnumLength.word)
                ,'unloadingrunning' : (109, EnumLength.bit)
                ,'unloadingfull' : (110, EnumLength.bit)
                ,'unloadingempty' : (111, EnumLength.bit)
                ,'filler1' : (32, EnumLength.byte)
                ,'filler2' : (40, EnumLength.bit)
                ,'filler3' : (41, EnumLength.bit)
                ,'filler4' : (42, EnumLength.bit)
                ,'filler5' : (43, EnumLength.bit)
                ,'filler6' : (44, EnumLength.bit)
                ,'filler7' : (64, EnumLength.byte)
                ,'filler8' : (72, EnumLength.bit)
                ,'filler9' : (73, EnumLength.bit)
                ,'filler10' : (74, EnumLength.bit)
                ,'filler11' : (75, EnumLength.bit)
                ,'filler12' : (76, EnumLength.bit)
                ,'filler13' : (96, EnumLength.byte)
                ,'filler14' : (104, EnumLength.bit)
                ,'filler15' : (105, EnumLength.bit)
                ,'filler16' : (106, EnumLength.bit)
                ,'filler17' : (107, EnumLength.bit)
                ,'filler18' : (108, EnumLength.bit)
                }
    messageBits = 112


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
    
    def getValue(self, name):
        ret = 0
        myName = name.lower().strip()
        if myName in self.protocol:
            index = self.protocol[myName][0]
            length = self.protocol[myName][1]
            myBits = self.bits[index: index + length]
            for myBit in myBits:
                ret = (ret << 1) | myBit            
            return ret
        else:
            return None
        
    def setMessage(self, message):
        self.reset()
        i = 0
        for myByte in message:
            myBits = self.numberToBits(myByte)
            self.bits[i * 8: (i +1)*8] = bitarray(myBits)
            i += 1
            
    def getLogMessages(self):
        ret = []
        for myKey in ('icr','errorack','acknack','sortingerror','sortingrunning','sortingwaiting','sortingfunction','z1error','z1running','z1waiting','z1function','unloadingrunning','unloadingfull','unloadingempty'):
            ret.append(myKey + ": " + str(self.getValue(myKey)))
        return ret
            
            
if __name__ == '__main__':           # self test code
    myMessage = RxMessage()
    myBytes = bytearray([72, 50, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    myMessage.setMessage(myBytes);
                  

