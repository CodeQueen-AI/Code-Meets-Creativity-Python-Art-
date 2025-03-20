from turtle import *
import colorsys
speed(0)

bgcolor("black")

h = 0.6

pensize(2)

for i in range(300):
    
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.005
    
    for j in range(2):
        
        fd(i * j* 2)
        lt(91)
        
done()