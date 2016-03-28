# -*- coding: UTF-8 -*-
from collections import Counter
"""
	Jinda Han @ March 16, 2015
	print text in each line
	function: txt_print_each_line(file_dir,file_start,file_end)
"""
file_dir = "files/"
file_out_dir = "network/"
file_start = 0
file_end_test = 3910
file_end = 3910
file_to_write_subtitle = "0-subtitle.txt"
#build a dictionary
subtitle_list = []


def txt_parse_subtitle(file_dir,file_start,file_end):
	f_out_1 = open(file_out_dir + "0-subtitle.txt","w")

	# open the file with read only permit
	for num in range (file_start, file_end):
		f = open(file_dir + str(num),"r") # file open
		for num, line in enumerate(f):
			line = line.split(": ")
			#print line[0]
			subtitle_list.append(line[0])

	counts = Counter(subtitle_list)
	#counts2 = counts.most_common()
	#print counts2
	#cmd+/
	# # sorted by name
	# for key, value in sorted(counts.items()):
	# 	print key, "\t",value
	# 	f_out_1.write(str(value) + "\t" + str(key) + "\n")

	# sorted by value
	for key, value in counts.most_common():
		print key, "\t",value
		f_out_1.write(str(value) + "\t" + str(key) + "\n")


	f_out_1.close
#function test
txt_parse_subtitle(file_dir,file_start,file_end_test)
