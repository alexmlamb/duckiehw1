import cv2
import sys
import numpy as np

img = cv2.imread(sys.argv[1])
filters = sys.argv[2].split(":")


def instagram(image, filter_lst):

    gen = image

    for f in filter_lst:
        if f == "flip-vertical":
            gen = gen[::-1]
        elif f == "flip-horizontal":
            gen = gen[:,::-1]
        elif f == "grayscale":
            gen = cv2.cvtColor(gen, cv2.COLOR_BGR2GRAY)
        elif f == "sepia":
            sepia_kernel = np.array([[.272,.534,.131],[.349,.686,.168],[.393,.769,.189]])
            gen = cv2.transform(gen, sepia_kernel)
        else:
            raise Exception('filter not found')

    return gen

gen = instagram(img, filters)

cv2.imwrite(sys.argv[3], gen)

