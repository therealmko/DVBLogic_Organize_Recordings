#########################################################################
#									#
# organize_recordings.py, to move recordings to user directories	#
# Initial version by King on 26-07-2013					#
# v1.0	King	26-07-2013						#
# v1.1  King	29-07-2013	Add file permission settings		#
# v1.2	King	30-07-2013	Add chowning file option		#
#									#
#########################################################################

from pwd import getpwnam
from os import listdir, chmod, chown
from os.path import isfile, join
from grp import getgrnam
import shutil

myCompareFile="organize_recordings.ini"
myPath="."

f = file(myCompareFile, "rb")    
lines = f.readlines()

for line in lines:
	vals = line.split(',')

	myFiles = [ myFile for myFile in listdir(myPath) if isfile(join(myPath,myFile)) ]
	myRecFiles = [ myRecFile for myRecFile in myFiles if myRecFile.find(vals[2].rstrip()) != -1 ]
	
	for myPersonalRec in myRecFiles:
		uid = getpwnam(vals[0]).pw_uid
		gid = getgrnam("users").gr_gid
		shutil.move(myPersonalRec, vals[1])
		chmod(vals[1] + "/" + myPersonalRec, 0777)
		chown(vals[1] + "/" + myPersonalRec, uid, gid)
		listdir(myPath)

f.close()
