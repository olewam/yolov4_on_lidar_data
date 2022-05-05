# Use the weight file trained on the datasyn dataset. Link to download in report
./darknet detector map ./data/datasyn.data ./cfg/datasyn.cfg ./backup/datasyn_14000.weights

# or

# ./darknet detector recall ./data/datasyn.data ./cfg/datasyn.cfg ./backup/*.weights