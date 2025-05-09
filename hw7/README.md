# Homework 7 – Alternative Model (YOLOv8)

## Model

- **Model:** YOLOv8n (Ultralytics)
- **Task:** Object detection of golf ball (center mass)
- **Dataset:** Custom golf ball detection dataset https://universe.roboflow.com/trungam/golf-fmo
- **Training epochs:** 50
- **Resolution:** 640x640

## Training Command

See `train_yolov8.sh` for full command.

## Prediction Command

See `predict_yolov8.sh` for inference example.
The `yolov8/models/yolov8n_best.pt` file will be used once training completes.

## Notes

- This model is used as an alternative to YOLOv7 (baseline).
- Training is being run in a Docker container using the official `ultralytics/ultralytics` image.
- Predictions will be generated on test images once the model is trained.
