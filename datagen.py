import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
import keras
from keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np
import glob
import os
def generate(source,dest,trans_per_image:int):
    x=1
    l=glob.glob("%s/*.jpg"%source)
    print(l)
    src_n=len(l)
    if not os.path.exists(dest):
        os.makedirs(dest)
    for j in range(src_n):
        img=cv2.imread(l[j],1)
        img=img.reshape(1,img.shape[0],img.shape[1],img.shape[2])
        gen=ImageDataGenerator(rotation_range=30,width_shift_range=0.1,fill_mode='reflect',height_shift_range=0.1,shear_range=0,zoom_range=0.1,horizontal_flip=True,vertical_flip=True)
        augiter=gen.flow(img)
        while x<=trans_per_image*j:
            cv2.imwrite('%s/%d.jpg'%(dest,x),next(augiter)[0].astype(np.uint8))
            print("Generation number : %i"%x,end='\r')
            x+=1
    print("\nDone")
generate("Fire images","augmented fire",10)
generate("Normal Images 1","augmented no fire",10)
