'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1A - Part 1 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_1a_part1.py
# Functions:		scan_image
# 					[ Comma separated list of functions in this file ]
# Global variables:	shapes
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
##############################################################


# Global variable for details of shapes found in image and will be put in this dictionary, returned from scan_image function
shapes = {}
adata  = []

################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################






##############################################################


def scan_image(warped_image):

    """
    Purpose:
    ---
    this function takes file path of an image as an argument and returns dictionary
    containing details of colored (non-white) shapes in that image

    Input Arguments:
    ---
    `img_file_path` :		[ str ]
        file path of image

    Returns:
    ---
    `shapes` :              [ dictionary ]
        details of colored (non-white) shapes present in image at img_file_path
        { 'Shape' : ['color', Area, cX, cY] }
    
    Example call:
    ---
    shapes = scan_image(img_file_path)
    """

    global shapes
    c=0
    ##############	ADD YOUR CODE HERE	##############
    shapes = dict()
    # print("1..")
    # img2 = cv2.imread(img_file_path)
    # print("2..")
    img2 = warped_image
    img = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) 
    # print("3..")
    _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY) 
    # print("4..")
    contours, _= cv2.findContours(threshold, cv2.RETR_TREE, 
                                cv2.CHAIN_APPROX_SIMPLE) 
    # print("5..")
    for cnt in contours : 
        # print("6..")
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
        # print("7..")
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 5)  
        # print("8..")
        M = cv2.moments(cnt)
        # print("9..")
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # print("10..")
        colour=[]
        # print("11..")
        colour.append(img2[cY,cX])
        # print("12..")
        if colour[0][0]>=128 and colour[0][1]<128 and colour[0][2]<128:
            # print("13..")
            color = 'blue' 
        elif colour[0][0]<120 and colour[0][1]>=128 and colour[0][2]<128:
            # print("14..")
            color = 'green'
        elif colour[0][0]<128 and colour[0][1]<128  and colour[0][2]>=128:
            # print("15..")
            color = 'red'
        else:
            color = 'none'
            # print("16..")

        area = cv2.contourArea(cnt)
        # print("17..")
        if len(approx)==3:
            # print("18..")
            shapes["Triangle"]=[color,cX,cY]      
        elif len(approx)==4:
            # print("19..")
            n = approx.ravel()  
            i = 0
            a=[]
            b=[]   
            for j in n : 
                if(i % 2 == 0): 
                    x = n[i] 
                    y = n[i + 1] 
                    a.append(x)
                    b.append(y)
                i = i + 1  
            # print("20..")
            if b[3]-b[0]==0 or a[1]==0 or b[3]==0 or a[2]==0 or b[1]==0:
                # print("21..")
                continue        
            l1= (((a[1]-a[0])**2)+((b[1]-b[0])**2))**0.5
            l2= (((a[2]-a[1])**2)+((b[2]-b[1])**2))**0.5
            l3= (((a[3]-a[2])**2)+((b[3]-b[2])**2))**0.5
            l4= (((a[0]-a[3])**2)+((b[0]-b[3])**2))**0.5
            d1= (((a[0]-a[2])**2)+((b[0]-b[2])**2))**0.5
            d2= (((a[1]-a[3])**2)+((b[1]-b[3])**2))**0.5
            pointRatiox1=float((a[0]/a[1])/(a[3]/a[2]))
            pointRatiox2=float((b[0]/b[3])/(b[1]/b[2]))
            # print("22..")
            aspectRatio =float((a[1]-a[0])/(b[3]-b[0]))
            if (((l1**2)+(l2**2)+(l3**2)+(l4**2))/((d1**2) + (d2 **2)) >=0.95) and (((l1**2)+(l2**2)+(l3**2)+(l4**2))/((d1**2) + (d2 **2)) <=1.05):
                if (aspectRatio >= 0.95 and aspectRatio <= 1.05):
                    if( area**0.5/l1 >= 0.95 and area**0.5/l1 <=1.05) and (area**0.5/l2 >=0.95 and area**0.5/l2 <=1.05 )and (area**0.5/l3 >=0.95 and area**0.5/l3<=1.05) and (area**0.5/l4 >= 0.95 and area**0.5/l4 <= 1.05) :
                        if color!='none':
                            shapes["Square"]=[color,cX,cY]
                            # print("23..")
                    elif (((area) /(d1 * d2 *0.5) )>=0.95) and ( ((area) /(d1 * d2 *0.5) )<=1.05)  :
                        if color!='none':
                            shapes["Rhombus"]=[color,cX,cY]
                            # print("24..")
                else:
                    if color!='none':
                        shapes["Parallelogram"]=[color,cX,cY]
                        # print("25..")
            

            elif (pointRatiox1 >=0.95 and pointRatiox1 <=1.05)  or (pointRatiox2 >=0.95 and pointRatiox2 <=1.05):
                if color!='none':
                    shapes["Trapezium"]=[color,cX,cY]
                    # print("26..")
            else: 
                if color!='none':
                    shapes["Quadrilateral"]=[color,cX,cY]
                    # print("27..")
        elif len(approx)==5:
            if color!='none':
                shapes["Pentagon"]=[color,cX,cY]
                # print("28..")
        elif len(approx)==6:
            print("hex")
            if color!='none':
                shapes["Hexagon"]=[color,cX,cY]
                # print("/29..")
        else:
           if color!='none':
                c+=1
                shape = "Circle"
                if c==1:
                    shapes['Circle']=[color,cX,cY]
                    adata.append([color,cX,cY])
                    
                elif c >1:
                    adata.append([color,cX,cY])

                    
                #   print("30..")
                # print("adata:",adata)
    
    if c>1:
        adata.sort()
        shapes[shape]=adata    

    # print("31..")
    # res=sorted(shapes.items(), key=lambda t: t[1][1], reverse = True)
    # print("32..")
    # shapes={}
    # for i,j in res[len(res)] :
    #     print("33..")
    #     shapes[i]=j
    # if cv2.waitKey(0) & 0xFF == ord('q'):  
    #     cv2.destroyAllWindows() 
	

	##################################################
    
    return shapes


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    the function first takes 'Sample1.png' as input and runs scan_image function to find details
#                   of colored (non-white) shapes present in 'Sample1.png', it then asks the user whether
#                   to repeat the same on all images present in 'Samples' folder or not

if __name__ == '__main__':

    curr_dir_path = os.getcwd()
    print('Currently working in '+ curr_dir_path)

    # path directory of images in 'Samples' folder
    img_dir_path = curr_dir_path + '/Samples/'
    
    # path to 'Sample1.png' image file
    file_num = 1
    img_file_path = img_dir_path + 'Sample' + str(file_num) + '.png'

    print('\n============================================')
    print('\nLooking for Sample' + str(file_num) + '.png')

    if os.path.exists('Samples/Sample' + str(file_num) + '.png'):
        print('\nFound Sample' + str(file_num) + '.png')
    
    else:
        print('\n[ERROR] Sample' + str(file_num) + '.png not found. Make sure "Samples" folder has the selected file.')
        exit()
    
    print('\n============================================')

    try:
        print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
        shapes = scan_image(img_file_path)

        if type(shapes) is dict:
            print(shapes)
            print('\nOutput generated. Please verify.')
        
        else:
            print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
            exit()

    except Exception:
        print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
        exit()

    print('\n============================================')

    choice = input('\nWant to run your script on all the images in Samples folder ? ==>> "y" or "n": ')

    if choice == 'y':

        file_count = 2
        
        for file_num in range(file_count):

            # path to image file
            img_file_path = img_dir_path + 'Sample' + str(file_num + 1) + '.png'

            print('\n============================================')
            print('\nLooking for Sample' + str(file_num + 1) + '.png')

            if os.path.exists('Samples/Sample' + str(file_num + 1) + '.png'):
                print('\nFound Sample' + str(file_num + 1) + '.png')
            
            else:
                print('\n[ERROR] Sample' + str(file_num + 1) + '.png not found. Make sure "Samples" folder has the selected file.')
                exit()
            
            print('\n============================================')

            try:
                print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
                shapes = scan_image(img_file_path)

                if type(shapes) is dict:
                    print(shapes)
                    print('\nOutput generated. Please verify.')
                
                else:
                    print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
                    exit()

            except Exception:
                print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
                exit()

            print('\n============================================')

    else:
        print('')
