#script for removing numbers from all file names in a folder

import os
def rename_files():
	# 1. get file names from a folder
	file_list = os.listdir("/Users/curtismitchell/udacity/prank")
	saved_path = os.getcwd()
	print("Current working directory is" + saved_path)
	os.chdir("/Users/curtismitchell/udacity/prank")

	# 2. for each file, rename file
	for file_name in file_list:
		print("old name" + file_name)
		print("new name" + file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_files()