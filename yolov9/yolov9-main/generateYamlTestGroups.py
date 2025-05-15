import os

TEMPLATE = """train: /train/images
val: data/valid/images
test: {test_path}

nc: 3
names: ['ball', 'club_head', 'fmo_ball']
"""

grouped_dir = "data/grouped_test"

for folder in os.listdir(grouped_dir):
    folder_path = os.path.join(grouped_dir, folder)
    images_path = os.path.join(folder_path, "images")
    if os.path.isdir(images_path):
        yaml_content = TEMPLATE.format(test_path=images_path)
        yaml_path = os.path.join(folder_path, "data.yaml")
        with open(yaml_path, "w") as f:
            f.write(yaml_content)
        print(f"Created: {yaml_path}")
