import rosbag
import sys
import numpy as np

bag_file = sys.argv[1]
n = int(sys.argv[2])
bag_out = rosbag.Bag(sys.argv[3], mode = 'w')

bag = rosbag.Bag(bag_file)

ind = 0

for topic, msg, t in bag.read_messages():

	if ind % n == 0:
		bag_out.write(topic=topic,msg=msg,t=t)

	ind += 1

bag.close()
bag_out.close()

