#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:08:36 2019

@author: Di Shen
"""

from PIL import Image
from pylab import *

im = array(Image.open("/Users/stephaniexia/Documents/didi/yinyuehui.jpg"))
imshow(im)
print('Please click 3 points')
imshow(im)
x = ginput(3)
print('You clicked:', x)

show()