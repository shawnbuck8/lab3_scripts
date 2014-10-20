import os

lab3_file = open('F:/TGIS_501/lab_3/GIS_is_the_best.txt', 'r')

newfile = open('F:/TGIS_501/lab_3/Corrected_GIS_is_the_best.txt', 'w+')

lab3_list = lab3_file.read()

ord_list = lab3_list.split(' ')

for words in ord_list:
	i = int(ord_list.index(words))
	if words == 'Science':
		del ord_list[i]
		ord_list.insert(i,'systems')
	elif words == 'science':
		del ord_list[i]
		ord_list.insert(i,'systems')

join_obj = ' '
newfile.write(join_obj.join(ord_list))

print "I'm Done...!"
lab3_file.close()
newfile.close()
