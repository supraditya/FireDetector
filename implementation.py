import cv2
import keras
import frame_enhancer as fe
from keras.models import load_model
model=load_model('val94.h5')
non_fire_img=cv2.imread('non fire test case.jpg',1)
fire_img=cv2.imread('fire test case.jpg',1)
non_fire_final=fe.enhance(non_fire_img)
fire_final=fe.enhance(fire_img)
a=cv2.resize(non_fire_final,(50,50))
a=a.reshape(1,50,50,3)
b=cv2.resize(fire_final,(50,50))
b=b.reshape(1,50,50,3)
print("For non fire image")
print(model.predict(a))
print("For fire image");
print(model.predict(b))


