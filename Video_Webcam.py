import cv2 as cv

class webcam:
    def __init__(self):
        self.webcam = cv.VideoCapture(0)
        self.frames = int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))
        self.currentFrame = 0
        self.CameraON = False

    def readCamera():
        status, frame = webcam.webcam.read()
        if(status == False) :
            webcam.CameraON = True
            return status, frame

    def showFrames():
        return webcam.frames

    def destroyCamera():
        webcam.webcam.release() # destroy the camera
        cv.destroyAllWindows() # destroy the window
        