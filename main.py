from ultralytics import YOLO

# 事前トレーニング済みモデルをロードします
model = YOLO("yolov8n.pt")
# Webカメラを起動
results = model(0 , show=True)