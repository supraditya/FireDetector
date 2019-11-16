import cv2 
import keras
from keras.models import load_model
import frame_enhancer as fe
model=load_model('val99.h5')

cap=cv2.VideoCapture('Fire video 1.mp4')
while True:
	ret,frame=cap.read()
	if not ret:
		break;
	frame1=fe.enhance(frame)
	a=cv2.resize(frame1,(50,50))
	a=a.reshape(1,50,50,3)
	p=model.predict(a)
	cv2.imshow('Original video',frame);
	cv2.imshow('Enhanced video',frame1);
	s=p[0]
	if s[0]>s[1]:
		print(p,end=" ");
		print("No Fire detected")
	else:
		print(p,end=" ");
		print("FIRE!!!")
	if cv2.waitKey(1000//24) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
