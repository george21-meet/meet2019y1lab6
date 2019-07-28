import turtle
import random
s=turtle.Screen()
s.colormode(255)
t=turtle.Turtle()
t.speed(0)
for i in range(1000):
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    t.color(r,g,b)
    t.circle(i)
    t.right(1)
