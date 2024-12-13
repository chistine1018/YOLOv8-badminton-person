# from ultralytics import YOLO
#
# # model = YOLO('../yolov8m.pt')
# #
# # model.train(data='data.yaml', epochs=20)
#
# # 創建 YOLO 模型
# model = YOLO("yolov8m.pt")  # 使用 Medium 模型
#
# # 開始訓練
# model.train(
#     data=f"{dataset.location}/data.yaml",  # 數據集配置路徑
#     epochs=20,                             # 訓練的 epoch 數量
#     imgsz=640                              # 圖片大小
# )
#
# model.val()
#
# !yolo task=detect mode=train model=yolov8m.pt data={dataset.location}/data.yaml epochs=20 imgsz=640



# from ultralytics import YOLO
# import os
# # os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
# # 創建 YOLO 模型
# model = YOLO("yolov8m.pt")  # 使用 Medium 模型
# # model.to('cuda')  # 移動模型到 GPU
#
# # 訓練數據集的路徑
# data_path = r"C:\Users\user\Downloads\交大\深度學習\LAB2\Test-2\data.yaml"
#
# # 開始訓練
# model.train(
#     data=data_path,  # 指定數據集配置的完整路徑
#     epochs=20,       # 訓練的 epoch 數量
#     imgsz=640        # 圖片尺寸
# )



from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

model = YOLO('yolov8n.pt')
model.train(data='data.yaml',
                      epochs=20,
                      # batch=64,
                      imgsz=640,
                      device=0,
                      workers=0
                      )
model.val()

# results = model("./test/images/06_mp4-0000_jpg.rf.61f83277d9de17e614072c758a18c7df.jpg")
# result = results[0]
# result.show()


