#Program to display negative of an image
import cv2
import numpy as np

def enhance(img):
	for k in range(1,543):
		img1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		for i in range(0,img.shape[0]):
			for j in range(0,img.shape[1]):
				img1[i][j][2]=(((np.cbrt(2*(img1[i][j][2]/255.0)-1)+1)/2)/2)*255.0
		img2=cv2.cvtColor(img1,cv2.COLOR_HSV2BGR)
		img2*=2
		return img2;