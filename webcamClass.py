import cv2

class webcam:

    def __init__(self):
        self.video = cv2.VideoCapture('./teste.mp4')
        self.frames = self.video.get(cv2.CAP_PROP_FPS)
    
    def ReadCamera(self):
       status, frame = self.video.read()
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
    