import glob
import os
import numpy as np

# Yolo needs a text file for every image. The script that writes the text files from the datasyn project does not make on for images without objects. 

current_dir = "/home/ascend/skole/yolov4_on_lidar_data/data/datasyn"

data_dir = "/home/ascend/skole/yolov4_on_lidar_data/data/datasyn/train"

for img_file in glob.iglob(os.path.join(data_dir, '*.png')): 
    have_file = False
    title, ext = os.path.splitext(os.path.basename(img_file))
    for txt_file in glob.iglob(os.path.join(data_dir, '*.txt')):
        if txt_file == os.path.join(title + '.txt'):
            have_file = True

    if have_file == False:
        open(os.path.join(data_dir + "/" + title + '.txt'), mode='a').close()
