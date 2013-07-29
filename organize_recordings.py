#########################################################################
#									#
# organize_recordings.py, to move recordings to user directories	#
# Initial version by King on 26-07-2013					#
# v1.0	King	26-07-2013						#
# v1.1  King	29-07-2013	Add file permission settings		#
#									#
#########################################################################

from os import listdir, chmod
from os.path import isfile, join
import shutil

myCompareFile="organize_recordings.ini"
myPath="."

f = file(myCompareFile, "rb")    
lines = f.readlines()

for line in lines:
	vals = line.split(',')

	myFiles = [ myFile for myFile in listdir(myPath) if isfile(join(myPath,myFile)) ]
	myRecFiles = [ myRecFile for myRecFile in myFiles if myRecFile.find(vals[1].rstrip()) != -1 ]
	
	for myPersonalRec in myRecFiles:
		shutil.move(myPersonalRec, vals[0])
		chmod(vals[0] + "/" + myPersonalRec, 0777)
		listdir(myPath)

f.close()
