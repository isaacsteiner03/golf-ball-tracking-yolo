#!/bin/bash

WEIGHTS="runs/train/yolov9-golf/weights/best.pt"
IMG=640
CONF=0.001
IOU=0.65

for folder in data/grouped_test/*/; do
  YAML_PATH="${folder}data.yaml"
  NAME="yolov9_test_$(basename $folder)"
  echo "Running val_dual on $(basename $folder)..."
  python val_dual.py \
    --weights "$WEIGHTS" \
    --data "$YAML_PATH" \
    --task test \
    --img "$IMG" \
    --conf "$CONF" \
    --iou "$IOU" \
    --name "$NAME"
done
