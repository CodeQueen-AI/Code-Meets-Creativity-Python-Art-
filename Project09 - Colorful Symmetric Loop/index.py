from turtle import *

import colorsys as cs

tracer(10)

bgcolor("black")

pensize(2)

h = 0

def graphic(a, n) : 
    
    circle(50 + n, 90)
    
    left(a)
    
    circle(50+n , 90)
    
penup()

goto(0, 30)

pendown()

for i in range(70) :
    
    c = cs.hsv_to_rgb(h, 1, 0.9)
    
    pencolor(c)
    
    graphic(90, i)
    
    graphic(180, i)
    
    graphic(90, i)
    
    h += 0.005
    
done()