import turtle
turtle.goto(0,0)
turtle.direction=None
def up():
    turtle.direction="Up"
    on_move()
    print("you pressed the up key")
def down():
    turtle.direction="Down"
    on_move()
    print("you pressed the down key")
def right():
    turtle.direction="Right"
    on_move()
    print("you pressed the right key")
def left():
    turtle.direction="Left"
    on_move()
    print("you pressed the Left key")
    
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(right,"Right")
turtle.onkey(left,"Left")
def on_move():
    if turtle.direction=="Up":
        new_x=turtle.xcor()
        new_y=turtle.ycor()
        turtle.goto(new_x,new_y+50)
    elif turtle.direction=="Down":
        new_x=turtle.xcor()
        new_y=turtle.ycor()
        turtle.goto(new_x,new_y-50)
    elif turtle.direction=="Right":
        new_x=turtle.xcor()
        new_y=turtle.ycor()
        turtle.goto(new_x+50,new_y)
    elif turtle.direction=="Left":
        new_x=turtle.xcor()
        new_y=turtle.ycor()
        turtle.goto(new_x-50,new_y)
up()
right()
left()
down()


turtle.listen()
    
