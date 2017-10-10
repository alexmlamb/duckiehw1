
import cv2
import sys

x = cv2.imread(sys.argv[1])

print x.shape

x_flip = x[::-1]

print x_flip.shape

cv2.imwrite("derp.jpg", x_flip)

