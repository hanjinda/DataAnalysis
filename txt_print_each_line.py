# -*- coding: UTF-8 -*-
"""
	Jinda Han @ March 16, 2015
	print text in each line
	function: txt_print_each_line(file_dir,file_start,file_end)
"""
file_dir = "files/"
file_start = 0
file_end_test = 1
file_end = 3910

def txt_print_each_line(file_dir,file_start,file_end):
	# open the file with read only permit
	for num in range (file_start, file_end_test):
		f = open(file_dir + str(num),"r") # file open
		for num, line in enumerate(f):
			print line

#function test
txt_print_each_line(file_dir,file_start,file_end_test)