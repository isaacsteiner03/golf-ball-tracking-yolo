# Golf Ball Tracking with YOLOv7 and YOLOv9

This project focuses on fine-tuning YOLOv7 and YOLOv9 object detection models to track golf balls in videos of golf swings. The goal is to create a lightweight and efficient golf ball tracking system using computer vision techniques.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Dataset](#dataset)
- [Training](#training)
  - [YOLOv7](#yolov7)
  - [YOLOv9](#yolov9)
- [Inference](#inference)
  - [YOLOv7](#yolov7-inference)
  - [YOLOv9](#yolov9-inference)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Project Overview

Golf ball tracking is a challenging task due to the small size, high speed, and motion blur of the ball in videos. This project leverages state-of-the-art YOLO (You Only Look Once) object detection models to detect and track golf balls, club heads, and fast-moving objects (FMO) in golf swing videos.

The project includes:

- Fine-tuning YOLOv7 and YOLOv9 models on a custom golf ball dataset.
- Comparing the performance of YOLOv7 and YOLOv9 on golf ball tracking.
- Evaluating metrics such as Intersection over Union (IoU), precision, and recall.

## Project Structure

The Project is structured under the two main folders that contain the code from the official yolo repositories.
/yolov7/
/yolov9/yolov9-main/

Other files in those repository are helper files used for creating the grouped data sets for t-test.

The repository also contains a Demo video, the ttest csv.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/isaacsteiner03/golf-ball-tracking-yolo.git
   cd golf-ball-tracking
   ```

2. Optional: Create Virtual Env
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. Install the required Python packages:
   ```
   `   pip install -r requirements.txt`
   ```
   Download the pretrained YOLOv7 and YOLOv9 model weights

## Dataset

The golf ball dataset is organized in YOLO format and includes:

images/train/ and labels/train/ for training.
images/valid/ and labels/valid/ for validation.
Grouped test datasets under data/grouped_test/.
The dataset configuration is defined in data/data.yaml

## Training

YOLOv7
To fine-tune YOLOv7 on the golf ball dataset:

```
python train.py --weights yolov7.pt --cfg yolov7.yaml --data data/data.yaml --epochs 150
```

YOLOv9
To fine-tune YOLOv9 on the golf ball dataset:

```
python train.py --weights yolov9-m.pt --cfg yolov9-m.yaml --data data/data.yaml --epochs 150
```

Note these are example commands, the actual path will be determined by where your trained model gets saved.

## Inference

YOLOv7 Inference
To run detection on a video using YOLOv7:

```
python detect.py --weights path/to/yolov7.pt --source path/to/images --conf 0.05
```

YOLOv9 Inference
To run detection on a video using YOLOv9:

```
python val_dual.py --weights yolov9.pt --data data.yaml --task test
```

Note these are example commands, the actual path will be determined by where your trained model gets saved.

# License

This project is licensed under the GPL-3.0 License. See the LICENSE.md file for details.

## Acknowledgments

Original YOLOv7 repository: https://github.com/WongKinYiu/yolov7
Original YOLOv9 repository: https://github.com/ultralytics/yolov5
Roboflow for public datasets https://universe.roboflow.com/trungam/golf-fmo/dataset/8.
License
This project is licensed under the GPL-3.0 License. See the LICENSE.md file for details.

## GenAI Prompts and Citation(s):

Prompt: Help me generate a read me for my overall project repository
Source: Github Copilot (GPT-4o), Result: This File with minor modifications by myself.
