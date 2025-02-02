'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:			[ NB_1940 ]
# Author List:		[ Sourabha G, Ashwin S Rao, Nithin Jaikar ]
# Filename:			task_1b.py
# Functions:		applyPerspectiveTransform, detectMaze, writeToCsv
# 					[blockwork,]
# Global variables:	
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, csv)               ##
##############################################################
import numpy as np
import cv2
import csv
##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
CELL_SIZE=50
def blockwork(img,coordinate,count):
# size =CELL_SIZE
	h = CELL_SIZE*(coordinate[0]+1)
	w = CELL_SIZE*(coordinate[1]+1)
	h0= CELL_SIZE*coordinate[0]
	w0= CELL_SIZE*coordinate[1]
	# print("h:",h)
	# print("h0:",h0)
	if count > 1 and count <10:
		block = img[h0:h+3,w0-3:w+3]
		# print("entered 1-10")
		csize = (h+3)-(h0)
		# print("csize:",csize)
		rsize = (w+3)-(w0-3)
	elif count == 1 :
		block = img[h0:h+6,w0:w+6]
		rsize = (w+6)-(w0)
		csize = (h+6)-(h0)
	elif count > 91 and count < 100:
		block = img[h0-3:h,w0-3:w+3]
		rsize = (w+3)-(w0-3)
		csize = (h)-(h0-3)
	elif count == 11 or count == 21 or count == 31 or count == 41 or count == 51 or count == 61 or count == 71 or count == 81 or count == 91:		
		if count == 91 :
			block = img[h0-3:h,w0:w+3]
			csize = (h)-(h0-3)
			# print("csize:",csize)
			rsize = (w+3)-w0
		else:
			# print("11gde")
			block = img[h0-3:h+3,w0:w+4]
			csize = (h+3)-(h0-3)
			rsize = (w+4)-(w0)
			# print("cs:",csize)
			# print("rs",rsize)

	elif count % 10 == 0 :
		if count == 10:
			block = img[h0:h+3,w0-3:w]	
			rsize = (w)-(w0-3)
			csize = (h+3)-(h0)
		elif count == 100:
			block = img[h0-3:h,w0-3:w]
			csize = (h)-(h0-3)
			rsize = (w)-(w0-3)
		else:
			block = img[h0-3:h+3,w0-3:w]
			csize = (h+3)-(h0-3)
			rsize =(w)-(w0-3)
	else :
		block = img[h0-3:h+3,w0-3:w+3]
		csize = (h+3)-(h0-3)
		# print(csize)
		rsize = (w+3)-(w0-3)

	val=0
	dc=0
	uc=0
	lc=0
	rc=0
	for i in range (int(rsize/2)-9,int(rsize/2)+9):
		for j in range (int(csize-1)-13,int(csize-1)):	
		
			s=block [j,i]
			if s[0]==0 or s[1]==0 or s[2]==0:
				dc+=1
	for i in range (int(rsize/2)-9,int(rsize/2)+9):
		for j in range (0,13):
			n=block [j,i]
			
			# print("entered d")
			# print("i:",i)
			# print("j:",j)
			# print(n)

			if n[0]==0 or n[1]==0 or n[2]==0:
				uc+=1
	# for i in range (int(rsize-1)-13,int(rsize-1)):
	# 	for j in range (int(csize/2)-9,int(csize/2)+9):
		
	for i in range (int(csize/2)-12,int(csize/2)+12):
		for j in range (int(rsize-1)-13,int(rsize-1)):
			# print("i:",i)
			# print("j:",j)
			e=block [i,j]
			# print(e)
			if e[0]==0 or e[1]==0 or e[2]==0:
				rc+=1
	for i in range (int(rsize/2)-9,int(rsize/2)+9):
		for j in range (0,13):
			w=block [i,j]
			if w[0]==0 or w[1]==0 or w[2]==0:
				lc+=1
	# print("cb:",count)
	# if count == 91:
	# cv2.imshow('image ',block)
	# print("ca:",count)

	# print("=========================================================")

	# print (dc,rc,uc,lc)
	if dc>10:
		val +=8
		# print("d = 8")
	if rc>10:
		val+=4
		# print("r = 4")
	if uc>10:
		val+=2
		# print("u = 2")
	if lc>10:
		val+=1
		# print("l = 1")

	# print("total val: ",val)
	# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
	return  val
##############################################################


def applyPerspectiveTransform(input_img):

	"""
	Purpose:
	---
	takes a maze test case image as input and applies a Perspective Transfrom on it to isolate the maze

	Input Arguments:
	---
	`input_img` :   [ numpy array ]
		maze image in the form of a numpy array
	
	Returns:
	---
	`warped_img` :  [ numpy array ]
		resultant warped maze image after applying Perspective Transform
	
	Example call:
	---
	warped_img = applyPerspectiveTransform(input_img)
	"""

	warped_img = None

	##############	ADD YOUR CODE HERE	##############
	img=input_img
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	_, bin = cv2.threshold(gray,105,255,1) 
	bin = cv2.dilate(bin, None) 
	bin = cv2.dilate(bin, None)
	bin = cv2.erode(bin, None)  
	bin = cv2.erode(bin, None)
	contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	rc = cv2.minAreaRect(contours[0])

	box = cv2.boxPoints(rc)
	x=[]
	y=[]
	for p in box:
		x.append(p[0])
		y.append(p[1])	
	# print("y3:",y[0])
	# pts1 = np.float32([[x[1],y[1]],[x[2],y[2]],[x[0],y[0]],[x[3],y[3]]])
	# pts1 = np.float32([[x[1]-3,y[1]-3],[x[2]+3,y[2]-3],[x[0]-3,y[0]+4],[x[3]+3,y[3]+3]])
	# pts1 = np.float32([[x[1]-2.5,y[1]-2.5],[x[2]+2.5,y[2]-2.5],[x[0]-2.5,y[0]+2.5],[x[3]+2.5,y[3]+2.5]])
	# pts1 = np.float32([[x[1]-3,y[1]-3],[x[2]+3,y[2]-3],[x[0]-3,y[0]+4],[x[3]+3,y[3]+3]])
	pts1 = np.float32([[x[1]-2,y[1]-2],[x[2]+2,y[2]-2],[x[0]-2,y[0]+2],[x[3]+2,y[3]+2]])
	pts2 = np.float32([[0,0],[500,0],[0,500],[500,500]])
	M = cv2.getPerspectiveTransform(pts1,pts2)
	warped_img = cv2.warpPerspective(img,M,(500,500))

	##################################################

	return warped_img


def detectMaze(warped_img):

	"""
	Purpose:
	---
	takes the warped maze image as input and returns the maze encoded in form of a 2D array

	Input Arguments:
	---
	`warped_img` :    [ numpy array ]
		resultant warped maze image after applying Perspective Transform
	
	Returns:
	---
	`maze_array` :    [ nested list of lists ]
		encoded maze in the form of a 2D array

	Example call:
	---
	maze_array = detectMaze(warped_img)
	"""

	maze_array = []

	##############	ADD YOUR CODE HERE	##############
	
	img= warped_img

	_, img = cv2.threshold(img,144,255,cv2.THRESH_BINARY)
	# cv2.imshow("w",img)
	binary_img = img
	
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	height, width,x= binary_img.shape
	no_cells_height = int(height/CELL_SIZE)							
	no_cells_width = int(width/CELL_SIZE)								
	# cb=0
	# ca=0y
	count=0
	maze_array = []
	for i in range (no_cells_height):
		maze_array.append([])
		for j in range(no_cells_width):
			sz = [i,j]
			count+=1
			# cb+=1
			val= blockwork(img, sz,count)
			maze_array [i].append(val)
	
	##################################################

	return maze_array


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
def writeToCsv(csv_file_path, maze_array):

	"""
	Purpose:
	---
	takes the encoded maze array and csv file name as input and writes the encoded maze array to the csv file

	Input Arguments:
	---
	`csv_file_path` :	[ str ]
		file path with name for csv file to write
	
	`maze_array` :		[ nested list of lists ]
		encoded maze in the form of a 2D array
	
	Example call:
	---
	warped_img = writeToCsv('test_cases/maze00.csv', maze_array)
	"""

	with open(csv_file_path, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(maze_array)


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function first takes 'maze00.jpg'
# 					as input, applies Perspective Transform by calling applyPerspectiveTransform function,
# 					encodes the maze input in form of 2D array by calling detectMaze function and writes this data to csv file
# 					by calling writeToCsv function, it then asks the user whether to repeat the same on all maze images
# 					present in 'test_cases' folder or not. Write your solution ONLY in the space provided in the above
# 					applyPerspectiveTransform and detectMaze functions.

if __name__ == "__main__":

	# path directory of images in 'test_cases' folder
	img_dir_path = 'test_cases/'

	# path to 'maze00.jpg' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')

	# path for 'maze00.csv' output file
	csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
	
	# read the 'maze00.jpg' image file
	input_img = cv2.imread(img_file_path)

	# get the resultant warped maze image after applying Perspective Transform
	warped_img = applyPerspectiveTransform(input_img)

	if type(warped_img) is np.ndarray:

		# get the encoded maze in the form of a 2D array
		maze_array = detectMaze(warped_img)

		if (type(maze_array) is list) and (len(maze_array) == 10):

			print('\nEncoded Maze Array = %s' % (maze_array))
			print('\n============================================')
			
			# writes the encoded maze array to the csv file
			writeToCsv(csv_file_path, maze_array)

			cv2.imshow('warped_img_0' + str(file_num), warped_img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		
		else:

			print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
			exit()
	
	else:

		print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
		exit()
	
	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

	if choice == 'y':

		for file_num in range(1, 10):
			
			# path to image file
			img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

			print('\n============================================')
			print('\nFor maze0' + str(file_num) + '.jpg')

			# path for csv output file
			csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
			
			# read the image file
			input_img = cv2.imread(img_file_path)

			# get the resultant warped maze image after applying Perspective Transform
			warped_img = applyPerspectiveTransform(input_img)

			if type(warped_img) is np.ndarray:

				# get the encoded maze in the form of a 2D array
				maze_array = detectMaze(warped_img)

				if (type(maze_array) is list) and (len(maze_array) == 10):

					print('\nEncoded Maze Array = %s' % (maze_array))
					print('\n============================================')
					
					# writes the encoded maze array to the csv file
					writeToCsv(csv_file_path, maze_array)

					cv2.imshow('warped_img_0' + str(file_num), warped_img)
					cv2.waitKey(0)
					cv2.destroyAllWindows()
				
				else:

					print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
					exit()
			
			else:

				print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
				exit()

	else:

		print('')

