lab3_file = open('F:/TGIS_501/lab_3/GIS_is_the_best.txt')
lab3_list = lab3_file.read()


total_words, sci_word, sys_word = 0 , 0 , 0


for words in lab3_list.split(' '):
	
	if words.lower() == 'science':
		sci_word = sci_word + 1
	elif words.lower() == 'systems':
		sys_word = sys_word + 1
	total_words = total_words + 1

print 'Total words = ' + str(total_words)
print 'Science = ' + str(sci_word)
print 'Systems = ' + str(sys_word)