
from roboflow import Roboflow

rf = Roboflow(api_key="iPtEZXUugxmVl2D5v8fm")
project = rf.workspace("yolo-lab2").project("test-skmj6")
version = project.version(3)
dataset = version.download("yolov8")
