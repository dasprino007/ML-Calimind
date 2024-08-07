import mediapipe as mp
from mediapipe.tasks import python
class Pose_Estimation:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_pose = mp.solutions.pose
        self.base_options = python.BaseOptions(model_asset_path='./model/pose_landmarker_full.task')