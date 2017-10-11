#!/usr/bin/env python
import rospy
from std_msgs.msg import String #Imports msg
from sensor_msgs.msg import CompressedImage

from duckietown_utils import rgb_from_ros, d8_compressed_image_from_cv_image, d8n_image_msg_from_cv_image
import cv2
import numpy as np

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
            raise Exception('filter not found: ' + f)

    return gen

# Initialize the node with rospy
rospy.init_node('instagram_thenuttynetter', anonymous=False)
# Create publisher

filters = rospy.get_param("~filters", "nope")

publisher = rospy.Publisher("topic/" +  filters.replace(":","_") + "/compressed",CompressedImage,queue_size=1)

filter_lst = filters.split(":")

def callback(msg):
	img = rgb_from_ros(msg)
	gen = instagram(img, filter_lst)
	newmsg = d8_compressed_image_from_cv_image(gen)
	publisher.publish(newmsg)

# Publish every 1 second
#while not rospy.is_shutdown():
#    msg = String()
#    msg.data = "Hello Duckietown!"
#    publisher.publish(msg)
#    rospy.sleep(1.0)

subscriber = rospy.Subscriber("/thenuttynetter/camera_node/image/compressed", CompressedImage, callback)

rospy.spin()



