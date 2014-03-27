'''
Created on Sep 27, 2013

@author: val3xiv
'''
import threading
import socket
import time
import datetime
from main.tools import Tools;
from sorting.settings.common import SOCKET_DATA
from rxmessage import RxMessage

class UdpServer(threading.Thread):
    '''
    Simple socket server
    '''


    def __init__(self, host, port, bufferlen=1024, objtools = None):
        '''
        Constructor
        '''
        super(UdpServer, self).__init__()
        self.host = host
        self.port = port
        self.addr = (host, port)
        self.bufferlen = bufferlen 
        self.lastmessage = RxMessage()
        self.ssock = None
        self.raddr = None
        self.received = False
        self.thisname = "UDP Server"
        self.tools = Tools() if objtools == None else objtools
        
    def handleconnection(self):
        '''
        Handle one incoming connection, from birth to death
        '''
        if self.ssock == None:
            self.ssock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
            self.ssock.bind(self.addr)
        try:
            data, address = self.ssock.recvfrom(self.bufferlen)
        except Exception, e:
            #print str(e)
            pass
        else:
            self.received = True
            self.raddr = address
            self.lastmessage.setMessage(bytearray(data))
            self.handlemessage(data)
        #self.close()
        """
        if not data:
            print "No data"
        else:
            self.handlemsg (data)
        """
    
    def handlemessage(self, data):
        '''
        Handle one incoming message
        '''
        mylog = []
        if not data:
            mylog.append("No date received")
            #print "\n[UDP Server " + str(datetime.datetime.now()) + "] No data received"
        else:
            mylog.append(str(len(data)) + " byte(s) received from " + str(self.raddr))
            mylog.append(list(bytearray(data)))
            mylog.extend(self.lastmessage.getLogMessages())
            #print "\n[UDP Server " + str(datetime.datetime.now()) + "] " + str(len(data)) + " byte(s) received from " + str(self.raddr) 
            #print list(bytearray(data))
        self.tools.printLog(self.thisname, mylog)
            
    def serve(self):
        '''
        Serve the port
        '''
        while 1:
            self.handleconnection()
            #time.sleep(1/1000)
            
    def close(self):
        if self.ssock:
            self.ssock.close()
            self.ssock = None
            
    def run(self):
        self.tools.printLog(self.thisname, ["Start"])
        #print '\n[UDP Server] listening....'    
        self.serve()
            
if __name__ == '__main__':           # self test code
    class echoserver (UdpServer):    # echo server
        def handlemessage (self, data):  # simply send back the message
            print "\n[" + str(datetime.datetime.now()) + "]\nReceived message: " + str(len(data)) + " byte(s) from " + str(self.raddr) 
            print list(bytearray(data))
            #self.sendmessage (data)

    echo = UdpServer('', SOCKET_DATA['myport'])
    echo.run()           
