import turtle as t
import colorsys  

t.bgcolor('black')
t.speed(0)  
h = 0.4  

for i in range(2000):
    c = colorsys.hsv_to_rgb(h, 1, 1) 
    h += 0.005

    t.width(5)
    t.pencolor(c) 

    t.fillcolor('black')
    t.begin_fill()

    t.forward(i)
    t.circle(120, steps=4)
    t.forward(i)
    t.right(91)

    t.forward(i)
    t.end_fill()

    t.forward(i)
    t.right(1)

t.done()


