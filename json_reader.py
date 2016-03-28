#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
	Jinda Han @ March 27, 2015
	reading and using JSON files
	You may ask questions on:
		how to print all the element from json in python?
		Iterating and printing JSON objects in Python?
		How to print particular JSON value in Python?
"""
import json
from pprint import pprint


if __name__ == '__main__':
	with open('classes_config.json') as data_file:    
		classes_config = json.load(data_file)
	for each_class in classes_config["classes"]:
		print each_class
		for each_class_element in classes_config["classes"][each_class]:
			print "\t" + each_class_element			
			if each_class_element == "keywords":
				for each_keywords in classes_config["classes"][each_class]["keywords"]:
					print "\t\t" + each_keywords

	# print(data)

