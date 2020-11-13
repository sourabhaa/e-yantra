import numpy as np
import cv2
import csv

# # def applyPerspectiveTransform(input_img):
# input
# print(input_img)
# img=Image.fromarray(input_img, 'RGB')
# imshow(img)


from numpy import asarray 
  
  
# load the image and convert into 
# numpy array 
img = cv2.imread('Sample2.png')
print(".")
print(img)
print("..")
# asarray() class is used to convert 
# PIL images into NumPy arrays 
# numpydata = asarray(img) 
  
# <class 'numpy.ndarray'> 
# print(type(numpydata)) 
  
#  shape 
# print(numpydata.shape) 
cv2.imshow("Sample2",img)
cv2.waitKey(0)
