import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
from keras.models import load_model
import cv2
import frame_enhancer as fe


model=load_model('val99.h5')

def predict(image):
	image = fe.enhance(image)
	image=cv2.resize(image,(50,50))
	image=image.reshape(1, 50, 50, 3)
	p=model.predict_classes(image)
	if p==0:
		return 'No Fire Detected'
	return 'Fire Detected'
