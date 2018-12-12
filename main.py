#!/usr/bin/env python
from scipy import *
from scipy.interpolate import interp1d
import cv2

def filename(prefix, count):
    return '/Users/Dennis/Desktop/tmp/' + prefix + '0'*(7-len(`count`)) + '%d.png' % count

hndl = open('scott.txt', 'wt')
stream = cv2.VideoCapture('video.mpg')
# video is 62 s long, 30 fps = 1860 frames

# interest is in 10 s to 30 s (frame 300 to 900)
# burn through the first 300 frames
for x in range(300):
    okay, image = stream.read()

# go through frames 300 to 900
for x in range(0, 600, 6):
    data = zeros([150, 3])
    for y in range(6):
        okay, image = stream.read()
        # print image.shape -> (720, 1280, 3)

        # crop_img = img[200:400, 100:300] # Crop from x,y,w,h -> 100,200,300,400
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
        # I want a region 600 wide x 450 tall
        cropped = image[85:535, 340:940]

        # take the average of all pixels across the horizontal direction
        binned = mean(cropped, axis=1)
        # now I've got a 450 x 3 (RGB) array

        # turn this 450 into 150
        for z in range(0,450,3):
            data[z/3,0] += (binned[z,0] + binned[z+1,0] + binned[z+2,0])/3.
            data[z/3,1] += (binned[z,1] + binned[z+1,1] + binned[z+2,1])/3.
            data[z/3,2] += (binned[z,2] + binned[z+1,2] + binned[z+2,2])/3.

    cv2.imwrite(filename('orig_', x), image)
    cv2.imwrite(filename('crop_', x), cropped)
    
    # write these 100 lines
    for z in range(150):
        hndl.write('%d %d %d, ' % (data[z,0]/6., data[z,1]/6., data[z,2]/6.))
    hndl.write('\n')
        



hndl.close()
