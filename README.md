# Bouncing-Objects

In this assignment, you will build a simulation where turtles move inside a bounded area. When turtles hit the boundary, they will “bounce” off the walls. You will implement two different movement systems:

Angle-based movement (heading system)

Coordinate-based movement (delta x / delta y system)

You will then extend the first system so that new turtles are created every time a wall is hit, creating a growing simulation.




Starter Requirements

Your program should include:

A screen setup (black background recommended)

A playing_area() function that draws the boundary box

A list to store all turtles in the simulation

Part 1: Playing Area
playing_area()

Create a function that draws a square boundary:

Size: approximately 480x480
Centered on the screen
Use a visible color (teal or similar)
The boundary should be filled or outlined clearly
Part 2: Movement Using Heading (Angle-Based)
move_with_heading(t, turtles)

Write a function that:

Moves the turtle forward continuously
Uses:
forward()
setheading()
heading()




Behavior Requirements:
The turtle should bounce off walls using reflection
Use angle reflection logic (like a mirror bounce




Extension Requirement (IMPORTANT)




When a turtle hits any wall:

Create a new turtle
Give it:
Random color
Triangle shape
Random starting direction
Speed of 0
Add it to a list of turtles
Return the updated list
Movement Using Delta X / Delta Y
move_with_deltas(t, dx, dy)

Write a function that moves a turtle using:

dx (change in x position)
dy (change in y position)




Behavior Requirements:

Update position using:
x = x + dx
y = y + dy
Use: 
t.goto(newX, newY)
Wall Collision Rules:

If hitting left or right wall:

Reverse dx

If hitting top or bottom wall:

Reverse dy

Return Values:

Return updated (dx, dy)

Main Simulation Loop

Your program should:

Store turtles in a list:

turtles = [starting_turtle]


Continuously update all turtles:

Loop through each turtle

Call move_with_heading()

When new turtles are created:

Add them to the list

They should immediately begin moving too

Expected Behavior
After completion:

One turtle starts moving

It bounces inside the box

Every time it hits a wall:

A new turtle appears

Over time:

The screen fills with many moving turtles
