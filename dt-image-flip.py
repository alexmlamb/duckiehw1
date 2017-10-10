
import cv2
import sys
import numpy as np

file_in = sys.argv[1]
outdir = sys.argv[2]

if outdir[-1] != "/":
  outdir += "/"

x = cv2.imread(file_in)

x_flip = x[::-1]

x_side_by_side = np.concatenate([x, x_flip], axis=1)


cv2.imwrite(outdir + "regular.jpg", x)

cv2.imwrite(outdir + "flip.jpg", x_flip)

cv2.imwrite(outdir + "side-by-side.jpg", x_side_by_side)

