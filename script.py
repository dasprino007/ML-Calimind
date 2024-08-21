# import the opencv library 
from webcamClass import webcam
import cv2 
import mediapipe as mp
import numpy as np
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

posetion = "NULL"
contador = 0

def calc_angle(x1, y1, x2, y2):
	x_diff = x1 - y1
	y_diff = x2 - y2
	return math.degrees(math.atan2(x_diff, y_diff))

# define a video capture object 
vid = webcam()
IsCameraOn = True
with mp_pose.Pose( min_detection_confidence=0.6, min_tracking_confidence=0.6) as pose:
	
	while(IsCameraOn): 
		ret, frame = vid.ReadCamera()

		# ChangeCvt()
		frame.flags.writeable = False
		image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		result = pose.process(image)

		image.flags.writeable = True
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		if result.pose_landmarks:
			mp_drawing.draw_landmarks(
				image,
				result.pose_landmarks,
				mp_pose.POSE_CONNECTIONS,
        		landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style(),
			)

		# teoricamente isso pegaria todos os pontos da pose
			poseList = []
			for id, im in enumerate(result.pose_landmarks.landmark):
				h, w, _ = image.shape
				X, Y = int(im.x * w), int(im.y * h)
				poseList.append([id, X, Y])

			if len(poseList) > 0:
				print(calc_angle(poseList[11][1], poseList[11][2], poseList[13][1], poseList[13][2]))
				if(poseList[11][2] and poseList[12][2] >= poseList[13][2] and poseList[14][2]):
					posetion = "down"

				elif((poseList[12][2] and poseList[11][2] <= poseList[14][2] and poseList[13][2]) and posetion == "down"):
					posetion = "NULL"
					contador = contador + 1
					print(contador)

		else:
			print("Pose not detected.")
		

		cv2.imshow('frame', cv2.flip(image, 1))
		if cv2.waitKey(1) & 0xFF == ord('q') | contador == 10:
			break
# After the loop release the cap object 
vid.CameraRelease()
del vid
# Destroy all the windows 
