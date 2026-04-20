from turtle import *
import random

# generates a random color
def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

# Creates the rectangular game boundary
def playing_area():
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("khaki")
    t.penup()
    t.goto(240,240)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.right(90)
        t.forward(480)
    t.end_fill()


# Function 1: Movement using turtle heading (forward + setheading)
def move_with_heading(t):
    # Move the turtle continuously using forward movement and its current heading.
    # The turtle should update its position each frame using forward().
    # When the turtle hits a boundary:
    #   - Use heading() to check its current direction.
    #   - Calculate the reflection angle based on the wall it hits.
    #   - Use setheading() to update the direction so it "bounces" off the wall.
    # The result should be smooth motion where direction is controlled by angles.
    t.forward(5)

    if t.xcor() > 240 or t.xcor() < -240:
        t.setheading(180 - t.heading())
        t.forward(10)
    if t.ycor() > 240 or t.ycor() < -240:
        t.setheading(-t.heading())


# Function 2: Movement using delta x / delta y (coordinate-based movement)
def move_with_deltas(t, deltax, deltay):
    # Move the turtle by directly updating its x and y position using dx and dy values.
    # Each update step:
    #   - Add deltax to x-coordinate and deltay to y-coordinate.
    # When the turtle hits a boundary:
    #   - Reverse deltax if it hits a left/right wall.
    #   - Reverse deltay if it hits a top/bottom wall.
    # This creates a bounce effect using vector-style movement instead of angles.
    # The turtle’s position should be updated using setx() and sety().
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

screen = Screen()
screen.title("Bouncing-objects")
screen.bgcolor("black")
screen.setup(520,520)

playing_area()


tur = Turtle()
tur.speed(0)
tur.color(generate_color())
tur.shape("circle")
tur.setheading(random.randint(0,360))
deltax = random.randint(-1,1) 
deltay = random.randint(-10,10) 




while True :
    deltax, deltay = move_with_deltas(tur, deltax, deltay)


screen.exitonclick()