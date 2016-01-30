#!/usr/bin/env python

'''
Author = Tasdik Rahman

Script to convert the text in the images to text and store it in particular directories in accordance 
to their names 
'''

#### Status : 
'''
Cleaning of the images done, running the tesseract OCR engine on the directory 
'''

#### Status

import os 

def main() : 
	## defining the directories which we have to work with 
	test_dir = r'/home/tasdik/Dropbox/projects/big_data_project/test'
	images_dir = r'/home/tasdik/Dropbox/projects/big_data_project/test/first_600_restaurants_dark'

	## get the list of directories (the hotels) and store it in a list 
	hotels_list = os.listdir('/home/tasdik/Dropbox/projects/big_data_project/test/first_600_restaurants_dark')

	## creating the test_menu_output folder if it does not exists
	menu_output_dir = r'/home/tasdik/Dropbox/projects/big_data_project/test/dark_ocr_menu_output'
	if not os.path.exists(menu_output_dir) : 
		os.makedirs(menu_output_dir)

	## walking through the files in the directory 
	for hotel in hotels_list : 
		hotel_dir = menu_output_dir + '/' + hotel
		## making the directory 
		os.makedirs(hotel_dir)
		print '#'*100
		print '\nchanged the directory to : ' + hotel_dir
		os.chdir(hotel_dir)

		## traversing the particular directory inside the images link
		hotel_images_directory = images_dir + '/' + hotel
		images_list = os.listdir(hotel_images_directory)
		new_images_list = [hotel_images_directory + '/' + x for x in images_list]
		## the above print command will print all the images for the particular hotel name with the absolute paths 

		########################################################################

		'''
		Now to automate the task of tesseract
		'''
		### traversing the images list 
		no_of_images = len(images_list)
		i = 0 
		for img in new_images_list : 
			image_name = images_list[i]
			new_image_name = image_name[:-4]
			print 'running OCR on  : '+image_name

			#####################################################
			### tesseract OCR Engine Code  			

			os.system('tesseract '+img+' '+ new_image_name)
			
			#####################################################
			
			i += 1

		########################################################################

if __name__ == '__main__' : 
	main()