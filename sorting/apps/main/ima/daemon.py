'''
Created on Nov 25, 2013

@author: val3xiv
'''
from sorting.settings.common import MEDIA_ROOT
import glob
import os.path
import time
from ima import Ima


while True:
	myImaPath = os.path.join(MEDIA_ROOT, "ima")
	if not os.path.isdir(myImaPath):
		myImaPath = os.path.join(MEDIA_ROOT, "myima")
	if os.path.isdir(myImaPath):
		myImaList = [myMember for myMember in glob.glob(os.path.join(myImaPath, "*")) if os.path.isfile(myMember)]
		for myMember in myImaList:
			myJsFile = os.path.join(MEDIA_ROOT, "js", os.path.basename(myMember) + ".js")
			if not os.path.exists(myJsFile):
				myIma = Ima(myMember, myJsFile)
	time.sleep(10)
