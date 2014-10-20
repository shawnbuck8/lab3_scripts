import os
import string

filepath = ('F:/TGIS_501/lab_3/text_files')

for root, dirs, files in os.walk(filepath):

	for f in files:

		f = f.lower()

		fil = f.split('.')

		if fil[1] == "txt":

			os.rename(filepath + f, "file_" + f)

		else:

			os.rename(filepath + f, "file_" + fil[0] + ".txt")

print 'Done!'


