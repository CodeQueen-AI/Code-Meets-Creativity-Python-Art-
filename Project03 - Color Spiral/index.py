from turtle import *
from colorsys import *

tracer(10)  
bgcolor('black')
pensize(3)
h = 0.9

goto(0, -140) 

for i in range(160):
    c = hsv_to_rgb(h, 1, 1) 
    h += 0.006
    color(*c) 

    circle(160 - i, 50)  
    left(40)  
    circle(160 - i, 70)
    right(70)

done()
