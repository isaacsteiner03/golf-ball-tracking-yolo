#!/bin/bash
# Run inference using the trained YOLOv8n model

yolo task=detect mode=predict \
  model=yolov8/models/yolov8n_best.pt \
  source=yolov8/data/test_images/ \
  conf=0.25