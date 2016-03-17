# -*- coding: UTF-8 -*-
"""
	Jinda Han @ March 16, 2015
	open the files from the directory
	classifier the line of files for building network
"""
# directory
file_dir = "files/"
file_out_dir = "network/"
file_start = 0
file_end_test = 10
file_end = 3910
file_to_write_name = "1-name.txt"
file_to_write_def = "2-definition.txt"
file_to_write_diag = "3-diagnosis.txt"
file_to_write_treat = "4-treatment.txt"
file_to_write_symp = "5-symptoms.txt"
file_to_write_causes = "6-causes.txt"
file_line_num = 1
# open all output files
f_out_1 = open(file_out_dir + "1-name.txt","w")
f_out_2 = open(file_out_dir + "2-definition.txt","w")
f_out_3 = open(file_out_dir + "3-diagnosis.txt","w")
f_out_4 = open(file_out_dir + "4-treatment.txt","w")
f_out_5 = open(file_out_dir + "5-symptoms.txt","w")
f_out_6 = open(file_out_dir + "6-causes.txt","w")

# open the file with read only permit
for num in range (file_start, file_end):
	f = open(file_dir + str(num),"r") # file open

	# read first eachline
	for num, line in enumerate(f):
		if num == 0:
			line = line.split("name: ")
			print line[1]
			f_out_1.write(str(file_line_num) + "\t" +line[1])

		if "Definition: " in line:
			line = line.split("Definition: ")
			print line[1]
			f_out_2.write(str(file_line_num + 10000) + "\t" +line[1])

		if "Symptoms and Signs: " in line:
			line = line.split("Symptoms and Signs: ")
			print line[1]
			f_out_3.write(str(file_line_num + 20000) + "\t" +line[1])

		if "Treatment: " in line:
			line = line.split("Treatment: ")
			print line[1]
			f_out_4.write(str(file_line_num + 30000) + "\t" +line[1])

		if "Causes: " in line:
			line = line.split("Causes: ")
			print line[1]
			f_out_5.write(str(file_line_num + 40000) + "\t" +line[1])

		if "Diagnosis: " in line:
			line = line.split("Diagnosis: ")
			print line[1]
			f_out_6.write(str(file_line_num + 50000) + "\t" +line[1])

	# for here if you want continuous number from file 1 to the end, 
	# then you need to separate the for loop and give each for loop a condition, 
	# and add in each loop if line[1] != "", then file_line_num += 1

	#end for


	file_line_num += 1
	f.close

#end for
f_out_1.close
f_out_2.close
f_out_3.close
f_out_4.close
f_out_5.close
f_out_6.close