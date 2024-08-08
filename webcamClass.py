import cv2

class webcam:

    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.frames = self.video.get(cv2.CAP_PROP_FPS)
        self.img_Height = 0.0
        self.img_width = 0.0
    
    def ReadCamera(self):
       status, frame = self.video.read()
       self.imgHeight = frame.shape[0]
       self.imgwidth = frame.shape[1]
       return status, frame
    
    def CameraRelease(self):
        self.video.release()
    
    def showFrames(self):
        return self.frames

    def showImage(self, image, flip):
        print("Imagem sendo transmitida")
        fliped_video = cv2.flip(image, flip)
        cv2.imshow('frame', fliped_video)

    def __del__(self):
        cv2.destroyAllWindows()
        print("camera foi de comes")
    