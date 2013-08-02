#########################################################################
#									#
# organize_recordings.py, to move recordings to user directories	#
# Initial version by King on 26-07-2013					#
# v1.0	King	26-07-2013						#
# v1.1  King	29-07-2013	Add file permission settings		#
# v1.2	King	30-07-2013	Add chowning file option		#
# v1.3  King    01-08-2013	Add check to not move current recordings#
#									#
#########################################################################

import pwd
import os
import time
import grp
import shutil

myCompareFile="organize_recordings.ini"
myPath="."

f = file(myCompareFile, "rb")    
lines = f.readlines()

for line in lines:
	vals = line.split(',')

	myFiles = [ myFile for myFile in os.listdir(myPath) if os.path.isfile(os.path.join(myPath,myFile)) ]
	myRecFiles = [ myRecFile for myRecFile in myFiles if myRecFile.find(vals[2].rstrip()) != -1 ]
	
	for myPersonalRec in myRecFiles:
		uid = pwd.getpwnam(vals[0]).pw_uid
		gid = grp.getgrnam("users").gr_gid

		fileCreation = os.path.getctime(myPersonalRec)		
		now = time.time()
		oneminute_ago = now - 60
		if fileCreation < oneminute_ago:
			print time.asctime( time.localtime(time.time()) ) + " : Moving " + myPersonalRec + " to " + vals[1]
			shutil.move(myPersonalRec, vals[1])
			os.chmod(vals[1] + "/" + myPersonalRec, 0777)
			os.chown(vals[1] + "/" + myPersonalRec, uid, gid)
	
f.close()

os.listdir(myPath)
