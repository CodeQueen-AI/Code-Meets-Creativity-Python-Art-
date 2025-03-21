from turtle import *

from colorsys import *

tracer(5)

bgcolor("black")

pensize(2)

h = 0

N = 190

pu()

goto(0, -200)

pu()

while(N!=0) :
    
    c = hsv_to_rgb(h, 1, 1)
    
    h += 1 / 30
    
    pencolor(c)
    
    fillcolor(c)
    
    left(49)
    
    pd()
    
    forward(N)
    
    pd()
    
    begin_fill()
    
    circle(N, 50)
    
    end_fill()
    
    N -= 1
    
done()