import os

folder = 'runs/detect/Run1-TestSetImages'
images = sorted(f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png')))

with open(os.path.join(folder, 'input.txt'), 'w') as f:
    for img in images:
        f.write(f"file '{img}'\n")
