# Golf Ball Tracking with YOLOv7

This project fine-tunes the YOLOv7 object detection model to detect golf balls in videos of golf swings. The goal is to create a lightweight golf ball tracking system using computer vision.

## Project Structure

```
golf-ball-tracking-project/
├── cfg/
├── models/
├── utils/
├── data/
│   ├── golf_ball_dataset/
│   └── golf.yaml
├── demo_videos/
├── results/
├── detect.py
├── train.py
├── test.py
├── requirements.txt
├── LICENSE.md
└── README.md
```

## Installation

1. Clone this repository.
2. (Optional) Create and activate a Python virtual environment.
3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Download the pretrained YOLOv7 model weights:

```bash
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
```

Place the `yolov7.pt` file in the project root directory.

## Dataset

The golf ball dataset is located under `data/golf_ball_dataset/`, organized in YOLO format:

- `images/train/`
- `images/valid/`
- `labels/train/`
- `labels/valid/`

The custom dataset configuration is defined in `data/golf.yaml`.

## Training

To fine-tune YOLOv7 on the golf ball dataset:

```bash
python train.py --workers 8 --device 0 --batch-size 16 --data data/golf.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --weights yolov7.pt --name golf-ball-finetune --hyp data/hyp.scratch.p5.yaml
```

Training outputs, including the best model checkpoint (`best.pt`), will be saved under `runs/train/golf-ball-finetune/`.

## Inference (Detection)

To run detection on a video using the fine-tuned model:

```bash
python detect.py --weights runs/train/golf-ball-finetune/weights/best.pt --conf 0.25 --img-size 640 --source path_to_your_video.mp4
```

Detection results will be saved under the `runs/detect/exp*/` directory.

## Results

The project compares:

- Baseline YOLOv7 detection performance
- Fine-tuned YOLOv7 detection performance on golf ball tracking

Evaluation metrics include Intersection over Union (IoU), precision, and recall.

## Acknowledgments

- Original YOLOv7 repository: [https://github.com/WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7)
- Roboflow for public datasets

## License

YOLOv7 is licensed under the GPL-3.0 License. This project maintains attribution to the original authors.
