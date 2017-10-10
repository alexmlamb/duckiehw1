import rosbag
import sys
import numpy as np

bag_file = sys.argv[1]

bag = rosbag.Bag(bag_file)

nmsg = {}
tlst = {}

def to_interval(lst):
	ilst = []
	for j in range(0, len(lst) - 1):
		ilst.append(lst[j+1] - lst[j])
	return ilst

for topic, msg, t in bag.read_messages():

	if not (topic in nmsg):
		nmsg[topic] = 0
		tlst[topic] = []

	nmsg[topic] += 1
	tlst[topic].append(t.to_sec())

for topic in tlst:
	iv = np.array(to_interval(tlst[topic]))
	print topic + ":"
	print "\tnum_messages:", nmsg[topic]
	print "\tperiod:"
	print "\t\tmin:", iv.min()
	print "\t\tmax:",iv.max()
	print "\t\taverage:",iv.mean()
	print "\t\tmedian:",np.median(iv)

bag.close()

