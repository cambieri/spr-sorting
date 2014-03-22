'''
Created on Mar 21, 2014

@author: val3xiv
'''
import socket
import time
import datetime
class UdpClientDebug(object):
    '''
    Simple socket client
    '''


    def __init__(self, host = None, port = None):
        '''
        Constructor
        '''
        self.host = '192.168.99.1'
        self.port = 2000
        self.addr = (self.host, self.port)
        self.udpsocket = None
        self.senddebug()
        
    def createsocket(self):
        if self.udpsocket == None:
            self.udpsocket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        
    def sendmessage(self, data):
        ret = None
        if not data:
            pass
        else:
            ret = self.udpsocket.sendto(data, self.addr)
        return ret
    
    def closesocket(self):
        if self.udpsocket:
            self.udpsocket.close()
            self.udpsocket = None
        
    def senddebug(self):
        myBytes = bytearray([14, 204, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1])
        self.createsocket()
        while 1:
            numbytes = self.sendmessage(myBytes)
            print "\n[" + str(datetime.datetime.now()) + "]\nSent message " + str(numbytes) + "byte(s)\n" , list(myBytes)
            time.sleep(1)
                                                                                 
if __name__ == '__main__':           # self test code
    mysock = UdpClientDebug()
        
        
        
