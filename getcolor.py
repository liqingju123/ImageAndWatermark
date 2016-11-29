
# -*- coding: utf-8 -*-

from PIL import Image
import re
path ="/Users/imac/Desktop/pngs/dst/1.png"
im = Image.open("/Users/imac/Desktop/pngs/dst/1.jpg")
w,h =im.size

im = Image.open("/Users/imac/Desktop/pngs/dst/1.jpg").load()
R,G,B = im[w/2,h/2]

grayLevel = R * 0.299 + G * 0.587 + B * 0.114;
print im[w/2-100,h/2-100]
if grayLevel >= 192:
    print  '浅色'
else:
    print '深色'
    
path_tags =re.match(r'^.*.(jpg|png|jpge)$', path)  
print path_tags



    

