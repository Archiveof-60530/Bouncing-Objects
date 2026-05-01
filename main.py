from turtle import *
import random


def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def playing_area():
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    t.color(generate_color())
    t.penup()
    t.goto(240,240)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.right(90)
        t.forward(480)
    t.end_fill()

def move_with_heading(t,turtles):
    t.forward(10)
    if t.xcor() > 240 or t.xcor()< -240:
        t.setheading(180-t.heading())
        t.forward(10)
        turtles.append(create_turtle())

    if t.ycor() > 240 or t.ycor() < -240:
        t.setheading(-t.heading())
        t.forward(10)
        turtles.append(create_turtle())
    return turtles

def create_turtle ():
    tur = Turtle()
    tur.speed(0)
    tur.color(generate_color())
    tur.shape("circle")
    tur.setheading(random.randint(0,360))
    return tur

def move_with_deltas(t, deltax, deltay):
    newx = t.xcor() + deltax
    newy = t.ycor() + deltay
    if newx > 240 or newx < -240:
        newx = t.xcor()
        deltax *= -1
    if newy > 240 or newy < -240:
        newy = t.ycor()
        deltay *= -1
    t.goto(newx,newy)
    return deltax, deltay



def create_player():
    global player
    player = Turtle()
    player.speed(0)
    player.color("white")
    player.shape("turtle")

def up():
    global player
    player.setheading(90)
    player.sety(player.ycor()+10)

def down():
    global player
    player.setheading(-90)
    player.sety(player.ycor()-10)

def right():
    global player
    player.right(10)
    # player.setheading(0)
    # player.setx(player.xcor()+10)

def left():
    global player
    player.left(10)
    # player.setheading(180)
    # player.setx(player.xcor()-10)


screen = Screen()
screen.title("Bouncing-objects")
screen.bgcolor("black")
screen.setup(520,520)
screen.listen()
screen.onkey(create_player,'space')
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down") 
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")               


playing_area()

player = None

tur = Turtle()
tur.speed(0)
tur.color(generate_color())
tur.shape("circle")
tur.setheading(random.randint(0,360))

turtles = [tur]








while True :
    if player != None:
        move_with_heading(player, turtles)
    for obj in turtles:
        turtles = move_with_heading(obj,turtles)
        if player != None and player.distance(obj) < 20:
            obj.hideturtle()
            turtles.remove(obj)





screen.exitonclick()
