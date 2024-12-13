
from roboflow import Roboflow
rf = Roboflow(api_key="iPtEZXUugxmVl2D5v8fm")
project = rf.workspace("yolo-lab2").project("test-skmj6")
version = project.version(2)
dataset = version.download("yolov8")


# LAB15
# from roboflow import Roboflow
# rf = Roboflow(api_key="J94Yk72AJS6Lm1sDIhs6")
# project = rf.workspace("intelligent-applications-of-deep-learning").project("lab2-02l1y")
# version = project.version(2)
# dataset = version.download("yolov8")