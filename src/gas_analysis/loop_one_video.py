import cv2
import os
from gas_analysis.gas_detection import gas_detector
from gas_analysis.motion_detection import motion_detector

dirname = os.path.join(os.path.dirname(__file__), "../../videos")
filename = os.path.join(dirname, "leak/MOV_1669.mp4")

video = cv2.VideoCapture(filename)  ### add path to file

while True:
    cap = video
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    # if gas_detector(cap) == 0:
    if motion_detector(cap) == 0:
        cap.release()
        break
