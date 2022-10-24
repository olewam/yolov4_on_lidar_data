# Use the weight file trained on the darpa dataset
./darknet detector map ./data/darpa.data ./cfg/darpa.cfg ./backup/datasyn_14000.weights

# or

# ./darknet detector recall ./data/datasyn.data ./cfg/datasyn.cfg ./backup/*.weights