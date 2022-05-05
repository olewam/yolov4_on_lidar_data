# Use the yolov weights trained on the datasyn dataset.
# Get a random .mp4 video and run this script to get FPS

./darknet detector demo data/datasyn.data cfg/datasyn.cfg ./backup/datasyn_backup_big_images/datasyn_14000.weights ../Downloads/traffic_crop.mp4 -dont_show -ext_output
