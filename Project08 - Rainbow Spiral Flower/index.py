from turtle import *

from colorsys import *

tracer(50)

bgcolor('black')

pensize(4)

h = 0

for i in range(70) : 
    
    for j in range(4) :
        
        color(hsv_to_rgb(h, 1, 1))
        
        h += 1/36
        
        circle(200 + j * 2, 60)
        
        forward(20)
        
        circle(200 + j * 2, 60)
        
        left(60)
        
    right(10)
    
done()