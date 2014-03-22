'''
Created on Mar 21, 2014

@author: val3xiv
'''
import SocketServer
import socket
import time
import datetime

class UdpServerDebug(SocketServer.BaseRequestHandler):
    '''
    Simple socket server    
    '''
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "\n[" + str(datetime.datetime.now()) + "]"
        print "from {}".format(self.client_address[0])
        print list(bytearray(data))
        #socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "", 2000
    server = SocketServer.UDPServer((HOST, PORT), UdpServerDebug)
    server.serve_forever()
