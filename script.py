# import the opencv library 
from Video_Webcam import webcam
import cv2 
import mediapipe as mp
from mediapipe.tasks import python

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
base_options = python.BaseOptions(model_asset_path='./model/pose_landmarker_full.task')

# define a video capture object
def startWebcamProcess():
	vid = webcam()
	with mp_pose.Pose(
		min_detection_confidence=0.5,
		min_tracking_confidence=0.5) as pose:
		while(webcam.CameraON): 
			ret, frame = vid.readCamera()

			# ChangeCVT()
			frame.flags.writeable = False
			image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			result = pose.process(image)

			image.flags.writeable = True
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

			# drawLandmarks()
			mp_drawing.draw_landmarks( 
				image,
				result.pose_landmarks,
				mp_pose.POSE_CONNECTIONS,
				landmark_drawing_spec =	mp_drawing_styles.get_default_pose_landmarks_style()
			)

			print(webcam.showFrames())
			
			cv2.imshow('frame', cv2.flip(image, 1))
			if cv2.waitKey(1) & 0xFF == ord('q'): 
				break

	# After the loop release the cap object 
	webcam.destroyCamera()

startWebcamProcess()