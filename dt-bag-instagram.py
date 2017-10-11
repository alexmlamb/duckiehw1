import rosbag
import sys
import numpy as np
from duckietown_utils import rgb_from_ros, d8_compressed_image_from_cv_image, d8n_image_msg_from_cv_image
import cv2

def instagram(image, filter_lst):

    gen = image

    for f in filter_lst:
        if f == "flip-vertical":
            gen = gen[::-1]
        elif f == "flip-horizontal":
            gen = gen[:,::-1]
        elif f == "grayscale":
            gen = cv2.cvtColor(gen, cv2.COLOR_BGR2GRAY).reshape((gen.shape[0], gen.shape[1], 1))
	    gen = np.concatenate([gen,gen,gen], axis=2)
        elif f == "sepia":
            sepia_kernel = np.array([[.272,.534,.131],[.349,.686,.168],[.393,.769,.189]])
            gen = cv2.transform(gen, sepia_kernel)
        else:
            raise Exception('filter not found')

    return gen

bag_file = sys.argv[1]
topic_sel = sys.argv[2]
filters = sys.argv[3].split(":")
bag_out = rosbag.Bag(sys.argv[4], mode="w")


bag = rosbag.Bag(bag_file)

for topic, msg, t in bag.read_messages():
	
	if topic == topic_sel:
		img = rgb_from_ros(msg)
		img = instagram(img, filters)
		msg = d8n_image_msg_from_cv_image(img, 'bgr8')
		bag_out.write(topic=topic,msg=msg,t=t)


bag.close()
bag_out.close()



