import cv2 as cv

class webcam:
    def __init__(self):
        self.webcam = cv.VideoCapture(0)
        self.frames = int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))
        self.currentFrame = 0
        self.CameraON = True

    def StartCamera():
        status, frame = webcam.webcam.read()

        if(status == False) :
            webcam.CameraON = True
            return status, frame
        
        webcam.CameraON = False
        print("A camera não funciono")

    def showFps():
        return webcam.frames

    def showWebcam(image, name, flip = 0):
        img = cv.flip(image, flip) # para que img fique certa
        cv.imshow(name, img)

    def destroyCamera():
        webcam.webcam.release() # destroy the camera
        cv.destroyAllWindows() # destroy the window
        