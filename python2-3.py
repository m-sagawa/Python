# -*- coding: Shift-JIS -*-

print('課題3')

from PIL import Image
im = Image.open('summer.jpg')
width, height = im.size

#print(width)
#print(height)

import math
g = math.gcd(width, height)

w = width / g
h = height / g

print(w, ' : ', h)