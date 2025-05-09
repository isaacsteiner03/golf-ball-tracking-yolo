from ultralytics import YOLO

model = YOLO('runs/detect/yolov8-golf/weights/best.pt')
model.predict(
    source='data/test/images',
    conf=0.25,
    save=True
)