#!/bin/bash

WEIGHTS="runs/train/yolov7-TrainedRun/weights/best.pt"
IMG_SIZE=640
CONF=0.05
IOU=0.65
DEVICE=0

for file in data/grouped_test/golf*/data.yaml; do
  DIRNAME=$(dirname "$file")
  NAME=$(basename "$DIRNAME")
  echo "Running test on $NAME ..."
  python test.py \
    --weights "$WEIGHTS" \
    --data "$file" \
    --img-size $IMG_SIZE \
    --conf-thres $CONF \
    --iou-thres $IOU \
    --device $DEVICE \
    --task test \
    --name "test_${NAME}"
done