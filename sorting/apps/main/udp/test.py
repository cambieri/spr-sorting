'''
Created on Mar 27, 2014

@author: val3xiv
'''

from sorting.settings.common import SOCKET_DATA
from sorting.settings.common import MEDIA_ROOT
import os
from main.tools import Tools;
import datetime
from shutil import copyfile
class Test(object):
    '''
    Test Class
    '''


    def __init__(self, objtools = None):
        '''
        Constructor
        '''
        self.thisname = "Test"
        self.tools = Tools() if objtools == None else objtools
        
    def movedelete(self, filename):
        ret = False
        myFilePath = os.path.join(MEDIA_ROOT, SOCKET_DATA['folder'], filename)
        if (not os.path.isfile(myFilePath)):
            print "File " + myFilePath + " non esiste"
        else:
            myBackupPath = os.path.join(MEDIA_ROOT, SOCKET_DATA['folderbackup'], filename + "." + str(datetime.datetime.now()).replace("-","").replace(" ", ".").replace(":",""))
            try:
                print "copy " + myFilePath + " TO " + myBackupPath
                copyfile(myFilePath, myBackupPath)
#                os.rename(myFilePath, myBackupPath)
            except Exception, e:
                print "RENAME: " + str(e)
            try:
                print "delete " + myFilePath
                os.remove(myFilePath)
            except Exception, e:
                print "DELETE: " + str(e)
            ret = True
        return ret 
    
                                                                                                 
if __name__ == '__main__':           # self test code
    mytools = Tools()
    mytest = Test(mytools)
    mytest.movedelete("testfile")
    
        
        
