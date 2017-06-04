# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:13:50 2017

@author: shubra
"""

coords = ([392.8, 356.4], [559.6, 404.8], [451.6, 186.0], [698.8, 239.6], [204.0, 243.2], [590.8, 263.2], [389.2, 448.4], [179.6, 371.2], [719.6, 205.2], [489.6, 442.0], [80.0, 139.2], [469.2, 367.2], [673.2, 293.6], [501.6, 409.6], [447.6, 246.0], [563.6, 216.4], [293.6, 274.0], [159.6, 182.8], [662.0, 328.8], [585.6, 376.8], [500.8, 217.6], [548.0, 272.8], [546.4, 336.8], [632.4, 364.8], [735.2, 201.2], [738.4, 190.8], [594.8, 434.8], [68.4, 254.0], [702.0, 193.6], [670.8, 244.0])
print (coords)
print("\n  Except the first")
print(coords[1:])
print("\n Only the First")
print(coords[0:1])
print("\n Add start at the end so that x1 != x2 and y1 != y2 ")
print(coords[1:] + coords[0:1] )
coords1 = zip(coords,coords[1:] + coords[0:1])
print("\n")
print(coords1)
import numpy as np
distances =0
for c1,c2 in coords1:
    x1,y1 = c1
    x2,y2 = c2
    distances = np.hypot(x1-x2,y1-y2)
    print("\n x=",x1,"x2=",x2,"y1=",y1,"y2=",y2," Square (x1-x2)", pow((x1-x2),2)," Square  y1-y2", pow((y1-y2),2))
    print("Calc Hyp",pow((pow((x1-x2),2)+pow((y1-y2),2)),.5),"Python Hyp",distances )