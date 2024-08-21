# import the opencv library 
from webcamClass import webcam
import cv2 
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

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

		mp_drawing.draw_landmarks(
			image,
			result.pose_landmarks,
			mp_pose.POSE_CONNECTIONS,
        	landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style(),
		)

		if result.pose_landmarks:
			pose_landmarks = result.pose_landmarks
			l_knee_x = pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x * vid.img_width
			print(l_knee_x)
		else:
			print("Pose landmarks not detected.")

		fps = vid.showFrames()
		print(fps)

		cv2.imshow('frame', cv2.flip(image, 1))
		if cv2.waitKey(1) & 0xFF == ord('q'): 
			break

# After the loop release the cap object 
vid.CameraRelease()
del vid
# Destroy all the windows 
