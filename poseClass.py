import mediapipe as mp
import cv2
from mediapipe.tasks import python

class Pose_Class:
    def __init__(self,running_mode ,min_detection_confidence, min_tracking_confidence):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_pose = mp.solutions.pose
        self.base_options = python.BaseOptions(model_asset_path='./model/pose_landmarker_full.task')
        self.min_detection_confidence= min_detection_confidence,
        self.min_tracking_confidence= min_tracking_confidence
        self.running_mode = running_mode
    
    def configPose(self):
        with self.mp_pose.Pose(self.running_mode, self.min_detection_confidence, self.min_tracking_confidence) as pose:
            return pose

    def changeCVT(self, frame, flags):
        frame.flags.writeable = flags
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return image
    
    def DrawLandmarks(self, image, result):
        self.mp_drawing.draw_landmarks(
			image,
			result.pose_landmarks,
			self.mp_pose.POSE_CONNECTIONS,
        	landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style(),
		)
    

