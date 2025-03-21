from turtle import Screen , Turtle

from colorsys import hsv_to_rgb

screen = Screen()

screen.bgcolor("black")

screen.tracer(50)

t = Turtle()

t.pensize(1.5)

t.hideturtle()

h = 0.0

for i in range(200) :
    
    t.color(hsv_to_rgb(h, 0.7, 1))
    
    h += 0.01
    
    t.forward(i * 1.5)
    
    t.left(95)
    
    t.forward(i * 0.5)
    
    t.right(100)
    
    t.forward(i / 3)
    
    for j in range(4):
        
        t.color('white')
        
        t.forward(j * 5)
        
        t.left(150)
        
screen.update()

screen.mainloop