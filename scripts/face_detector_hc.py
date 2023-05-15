import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
sys.path.append('../')
from scripts.face_detector_fr import show


print(f"OpenCV version {cv2.__version__}")
print(f"Numpy version {np.__version__}")


def detect_face(image: np.ndarray, show: bool=False):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Load the HaarCascade Classifier with a correspongin config
    face_detector = cv2.CascadeClassifier('../config/haarcascade_frontalface_default.xml')
    
    # Detect faces
    results = face_detector.detectMultiScale(image)
    for (x, y, w, h) in results:
        cv2.rectangle(img=image,
                    pt1=(x, y),
                    pt2=(x+w, x+y),
                    color=(0, 255, 0),
                    thickness=2)
    
    image_aux = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    
    # Show the results
    if show:
        plt.imshow(image)
        plt.show()
