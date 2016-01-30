#!/usr/bin/env python

'''
Author : Tasdik Rahman

To read the .txt files inside the hotel folders and then append all those files into a single file 
in accordance to the name of the file
'''

import os 

def main() : 
	## reading the first file named "dark_ocr_menu_output"

	dark_file = '/home/tasdik/Dropbox/projects/big_data_project/test/light_ocr_menu_output'
	dest_file = '/home/tasdik/Dropbox/projects/big_data_project/test/all_menu_light'

	if not os.path.exists(dest_file) : 
		os.makedirs(dest_file)

	hotels_list = os.listdir('/home/tasdik/Dropbox/projects/big_data_project/test/light_ocr_menu_output')

	### reading the dark first file 

	for hotel in hotels_list : 
		hotel_dir = dark_file + '/' + hotel
		# print hotel_dir

		print '#'*70
		print 'changed the directory to ::: ' + hotel_dir
		images_list = os.listdir(hotel_dir)

		parent_file = images_list[0]
		parent_file_path = hotel_dir + '/' + parent_file 
		print "parent_file_path : " + parent_file_path
		print '\n'
		
		## skipping the first item in the images list 
		iterimages = iter(images_list)
		next(iterimages)

		## open the parent file with append mode

		open_parent_file = open(parent_file_path, 'r')
		parent_file_content = open_parent_file.read()
		open_parent_file.close()

		final_dest_file = dest_file + "/" + hotel + ".txt"

		print 'final folder : ' + final_dest_file
		# command = 'touch '+final_dest_file
		# os.system(command)

		os.mknod(final_dest_file)

		f = open(final_dest_file, 'w')  
		f.write(parent_file_content)
		f.close()

		print 'the other images are : '
		for img in iterimages : 
			img_dir = hotel_dir + '/' + img

			temp_file = open(img_dir, 'r')
			content = temp_file.read()

			with open(final_dest_file, 'a') as f : 
				f.write(content)
			### opening the first file in the list and then appending the list of  other files in the list of images
			# with open(parent_file_path + '.txt', 'a') as f : 
						
if __name__ == '__main__' : 
	main()