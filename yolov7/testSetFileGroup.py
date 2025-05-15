import os
import shutil

image_dir = 'data/test/images'
label_dir = 'data/test/labels'
output_base = 'data/grouped_test'

os.makedirs(output_base, exist_ok=True)

for fname in os.listdir(image_dir):
    if not fname.endswith('.jpg'):
        continue

    if fname.startswith("yt-"):
        group = 'yt_misc'
    else:
        group = fname.split('_')[0]

    group_dir_images = os.path.join(output_base, group, 'images')
    group_dir_labels = os.path.join(output_base, group, 'labels')
    os.makedirs(group_dir_images, exist_ok=True)
    os.makedirs(group_dir_labels, exist_ok=True)

    shutil.copy(os.path.join(image_dir, fname), os.path.join(group_dir_images, fname))

    label_file = fname.replace('.jpg', '.txt')
    src_label_path = os.path.join(label_dir, label_file)
    dst_label_path = os.path.join(group_dir_labels, label_file)
    if os.path.exists(src_label_path):
        shutil.copy(src_label_path, dst_label_path)
