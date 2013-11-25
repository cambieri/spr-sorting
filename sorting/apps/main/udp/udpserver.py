'''
Created on Sep 27, 2013

@author: val3xiv
'''
import socket

class UdpServer(object):
    '''
    Simple socket server
    '''


    def __init__(self, host, port, bufferlen=1024):
        '''
        Constructor
        '''
        self.host = host
        self.port = port
        self.addr = (host, port)
        self.bufferlen = bufferlen 
        
    def handleconnection(self):
        '''
        Handle one incoming connection, from birth to death
        '''
        stat = self.ssock.recvfrom(self.bufferlen)
        data, self.raddr = stat
        if not data:
            print "No data"
        else:
            self.handlemsg (data)
    
    def handlemessage(self, data):
        '''
        Handle one incoming message
        '''
        if not data:
            print "Client has exited"
        else:
            print "\nReceived message '", data, "'"
            
    def sendmessage(self, data):
        self.ssock.sendto(data, self.raddr)
            
    def serve(self):
        '''
        Serve the port

        '''
        while 1:
            self.ssock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
            self.ssock.bind(self.addr)
            self.handleconnection()
            self.ssock.close()
            
if __name__ == '__main__':           # self test code
    class echoserver (UdpServer):    # echo server
        def handlemsg (self, data):  # simply send back the message
            print "\nReceived message '", data, "'"
            #self.sendmessage (data)

    echo = echoserver ('', 9090)
    print 'Serving....'    
    echo.serve()           
