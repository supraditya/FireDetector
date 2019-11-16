import keras
from keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np
def generate(source,src_n:int,dest,trans_per_image:int):
    x=1
    for j in range(1,src_n+1):
        img=cv2.imread('%s/%d.jpg'%(source,j))
        img=img.reshape(1,img.shape[0],img.shape[1],img.shape[2])
        gen=ImageDataGenerator(rotation_range=30,width_shift_range=0.1,fill_mode='reflect',height_shift_range=0.1,shear_range=0,zoom_range=0.1,horizontal_flip=True,vertical_flip=True)
        augiter=gen.flow(img)
        while x<=trans_per_image*j:
            cv2.imwrite('%s/%d.jpg'%(dest,x),next(augiter)[0].astype(np.uint8))
            print("Generation number : %i"%x)
            x+=1
    print("Done")
generate("New Fire Images",110,"Fire 1",10)