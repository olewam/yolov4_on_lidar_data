# ./darknet detector test ".data file" ".cfg file" "your weights" "image to test on"
# Remember to change the weight file to the one trained on the datasyn dataset
./darknet detector test ./data/datasyn.data ./cfg/datasyn.cfg ./yolov4.weights data/datasyn/val/trip007_glos_Video00016_90.png -i 0 -thresh 0.25 























