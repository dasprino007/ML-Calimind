import cv2

class webcam:

    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def ReadCamera(self):
       status, frame = self.video.read() 
       return status, frame