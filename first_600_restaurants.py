#!/usr/bin/env python

'''
Author : Tasdik Rahman

To get the name of the first 700 restaurants in the file "burrp_bangalore.txt" and then move the files in 
"images" directory to another directory called "first_600_restaurants" 
'''

import os
from distutils.dir_util import copy_tree

def main(): 
	burrp_bangalore = r'/home/tasdik/Dropbox/projects/big_data_project/test/burrp_bangalore.txt'
	
	full_hotel_list = []

	with open(burrp_bangalore, 'r') as file : 
		for link in file : 
			temp_link = link.replace('http://www.burrp.com/bangalore/','')
			## splitting the temp_link for removing the restaurant id after the '/'
			var = temp_link.rpartition('/')[0]
			# print var
			## the above print statement prints out all the hotel names in the burrp_bangalore.txt

			## now to store it the list 
			full_hotel_list.append(var)


	final_hotel_list = full_hotel_list[:700]
	## now to move the files 
	print 'moving the files'

	dest_dir = r'/home/tasdik/Dropbox/projects/big_data_project/test/first_600_restaurants'
	
	## creating the directory if its not there
	if not os.path.exists(dest_dir) :
		os.makedirs(dest_dir)

	img_dir = r'/home/tasdik/Dropbox/projects/big_data_project/test/images'

	# print 'changing directory to : ' + dest_dir
	# os.chdir(dest_dir)

	for hotel in final_hotel_list : 
		print '#'*50
		print 'moving file \"' + hotel + '\"'
		src_path = img_dir + '/' + hotel

		final_dest_dir = dest_dir + '/' + hotel
		########################################3
		### os module which is not working 
		
		# copy_command = 'cp ' + src_path + ' ' + dest_dir + '/'
		# os.system('cp '+ src_path + ' ' + dest_dir)
		
		########################################3

		copy_tree(src_path, final_dest_dir)
		print '\n'

	print 'files moved!!!'

if __name__ == '__main__' : 
	main()