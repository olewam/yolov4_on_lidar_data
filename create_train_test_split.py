import glob
import os

current_dir = "/home/ascend/skole/yolov4_on_lidar_data/data/" # PATH TO IMAGE DIRECTORY# Percentage of images to be used for the valid set

train_data_dir = "/home/ascend/skole/yolov4_on_lidar_data/data/datasyn/train"
val_data_dir = "/home/ascend/skole/yolov4_on_lidar_data/data/datasyn/val"

file_train = open('datasyn_train_set.txt', 'a')  
file_test = open('datasyn_val_set.txt', 'a')

for file in glob.iglob(os.path.join(train_data_dir, '*.png')): 
    title, ext = os.path.splitext(os.path.basename(file))
    file_train.write(train_data_dir + "/" + title + '.png' + "\n")

for file in glob.iglob(os.path.join(val_data_dir, '*.png')): 
    title, ext = os.path.splitext(os.path.basename(file))
    file_test.write(val_data_dir + "/" + title + '.png' + "\n")


