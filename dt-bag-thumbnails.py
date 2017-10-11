import rosbag
import sys
import numpy as np
from duckietown_utils import rgb_from_ros
import cv2

bag_file = sys.argv[1]
topic_sel = sys.argv[2]
outdir = sys.argv[3]

if outdir[-1] != "/":
	outdir += "/"

bag = rosbag.Bag(bag_file)
ind = 0

for topic, msg, t in bag.read_messages():
	

	if topic == topic_sel:
		img = rgb_from_ros(msg)
		cv2.imwrite(outdir + str(ind).zfill(5) + ".jpg", img)
		ind += 1

bag.close()

