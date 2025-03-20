from turtle import *
from colorsys import *

speed(0)
bgcolor('black')
pensize(2)
tracer(10)

hue = 0 
penup()
goto(-50, -50)  
pendown()

for j in range(72):
    hue += 0.02 
    color(hsv_to_rgb(hue, 1, 1))  

    for i in range(12): 
        forward(i * 3) 
        right(45)  
        forward(i * 2)  
        right(60)  
        forward(i * 3)  
        left(120)  

    right(5) 

done()
