#!/usr/bin/env python
from scipy import *
from scipy.misc import imsave

hndl = open('scott.txt', 'rt')
data = hndl.readlines()
for frame in range(len(data)):
    img = zeros([150, 30, 3])
    pixels = data[frame].split(',')[:-1]
    y = 0
    for p in pixels:
        r, g, b = p.split()
        for x in range(30):
            img[y,x,0] = r
            img[y,x,1] = g
            img[y,x,2] = b
        y += 1

    imsave('/Users/dennis/Desktop/tmp/strip_%s%d.png' % ('0'*(3-len(`frame`)),frame), img) 
