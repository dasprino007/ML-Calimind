# import the opencv library 
from webcamClass import webcam
import cv2 
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

poseList = []
pose = "NULL"
contador = 0

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
			pose_landmarks = result.pose_landmarks
			mp_drawing.draw_landmarks(
				image,
				result.pose_landmarks,
				mp_pose.POSE_CONNECTIONS,
        		landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style(),
			)

		# teoricamente isso pegaria todos os pontos da pose
			for id, im in enumerate(pose_landmarks.landmark):
				X, Y = int(im.x * vid.img_width), int(im.y * vid.img_Height)
				poseList.append([id, X, Y])

			print(poseList)
   
			if len(poseList) != 0:
				if(poseList[11][2] and poseList[12][2] >= poseList[13][2] and poseList[14][2]):
					print(poseList[11][2], poseList[13][2])
					pose = "down"

				if((poseList[12][2] and poseList[11][2] <= poseList[14][2] and poseList[13][2]) and pose == "down"):
					print("contar 1")
					pose = "NULL"
					contador =+ 1

		else:
			print("Pose not detected.")
		

		cv2.imshow('frame', cv2.flip(image, 1))
		if cv2.waitKey(1) & 0xFF == ord('q') | contador == 10:
			break

# After the loop release the cap object 
vid.CameraRelease()
del vid
# Destroy all the windows 
