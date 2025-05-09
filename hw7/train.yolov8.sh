#!/bin/bash
# Train YOLOv8n model on golf ball dataset

yolo task=detect mode=train \
  model=yolov8n.pt \
  data=yolov8/data/data.yaml \
  epochs=50 \
  imgsz=640 \
  name=golf-yolov8
