'''
Created on Sep 27, 2013

@author: val3xiv
'''
import socket
class UdpClient(object):
    '''
    Simple socket client
    '''


    def __init__(self, host, port, bufferlen=1024):
        '''
        Constructor
        '''
        self.host = host
        self.port = port
        self.addr = (host, port)
        self.bufferlen = bufferlen
        
    def createsocket(self):
        self.udpsocket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        
    def sendmessage(self, data):
        if not data:
            pass
        else:
            self.udpsocket.sendto(data, self.addr)
        self.udpsocket.close()
                        
if __name__ == '__main__':           # self test code
    mysock = UdpClient('', 9090)
    def_msg = "===Enter message to send to server===";
    print "\n", def_msg
    # Send messages
    while (1):
        data = raw_input ('>> ')
        if not data:
            break
        else:
            mysock.createsocket()
            mysock.sendmessage(data)
        
        
        
