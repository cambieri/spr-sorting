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
    messageBytes = 66
    indexIc = 0
    lenIc = EnumLength.word
    indexFunction = 2
    lenFunction = EnumLength.word
    indexSuctionCupGroup1 = 6
    lenSuctionCupGroup1 = EnumLength.byte
    indexSuctionCupGroup2 = 7
    lenSuctionCupGroup2 = EnumLength.byte
    indexSuctionCupGroup3 = 8
    lenSuctionCupGroup3 = EnumLength.word
    indexSuctionCupGroup4 = 10
    lenSuctionCupGroup4 = EnumLength.word
    indexSuctionCupGroup5 = 12
    lenSuctionCupGroup5 = EnumLength.byte
    indexSuctionCupGroup6 = 13
    lenSuctionCupGroup6 = EnumLength.byte
    indexPlateuSxTaking = 22
    lenPlateuSxTaking = EnumLength.byte
    indexPlateuDxTaking = 23
    lenPlateuDxTaking = EnumLength.byte
    indexXquoteTaking = 26
    lenXquoteTaking = EnumLength.doubleWord
    indexYquoteTaking = 30
    lenYquoteTaking = EnumLength.doubleWord
    indexPlateuSxLeaving = 42
    lenPlateuSxLeaving = EnumLength.byte
    indexPlateuDxLeaving = 43
    lenPlateuDxLeaving = EnumLength.byte
    indexXquoteLeaving = 44
    lenXquoteLeaving = EnumLength.doubleWord
    indexYquoteLeaving = 48
    lenYquoteLeaving = EnumLength.doubleWord
    indexZquoteLeaving = 52
    lenZquoteLeaving = EnumLength.doubleWord
    indexIc1 = 64
    lenIc1 = EnumLength.word


    def __init__(self):
        '''
        Constructor
        ''' 
        self.reset()
    
    def reset(self):
        self.bits = bitarray(self.messageBytes * 8)
        self.bits.setall(False)        
        pass
    
    def numberToBits(self, num, length = EnumLength.byte):
        return bin(num)[2:].zfill(length)[-length:]
    
    def setValue(self, name, value):
        if hasattr(self, 'index' + name) and hasattr(self, 'len' + name):
            index = getattr(self, 'index' + name)
            length = getattr(self, 'len' + name)
            myBits = bitarray(self.numberToBits(value, length))
            self.bits[-(index + 1) * 8:length] = myBits
            return EnumResult.ok
        else:
            return EnumResult.dataUnexpected    
    
if __name__ == '__main__':           # self test code
    myMessage = TxMessage()
    """
    if hasattr(myMessage, 'indexIc'):
        print "ok"
    else:
        print "no"
    """
    print (myMessage.setValue("Ic", 32000) == EnumResult.ok)
    print myMessage.bits
                  

        