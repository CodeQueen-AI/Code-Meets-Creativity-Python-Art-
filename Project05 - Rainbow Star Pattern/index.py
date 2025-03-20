

from turtle import *

from colorsys import hsv_to_rgb

bgcolor('black')

tracer(5)

pensize(4)

h = 0

for i in range(100):
    
    color(hsv_to_rgb(h * 2, 1, 1))
    
    h += 0.01
    
    forward(i * 2)
    
    right(144)
    
    backward(i)
    
    right(144)
    
    forward(i * 2)
    
    left(144)
    
done()