import turtle
import random
import math
import time

# Create a window
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the player turtle
player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.penup()
player.speed(0)  # Set the initial speed to 0
pspeed = 1  # Initial player speed
player.speed(pspeed)
enemspeed = 1  # Initial enemy speed

# Create enemy turtles
p2 = turtle.Turtle()
p2.shape("triangle")
p2.color("red")
p2.penup()
p2.setposition(220, 0)
p2.left(180)
p2.speed(10)  # Set enemy speed

p3 = turtle.Turtle()
p3.shape("triangle")
p3.color("red")
p3.penup()
p3.setposition(p2.xcor() + 50, 0)
p3.left(180)
p3.speed(5)  # Set enemy speed

# Create a border
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.setposition(-300, -300)
pen.pendown()
pen.pensize(5)
pen.setposition(300, -300)
pen.setposition(300, 300)
pen.setposition(-300, 300)
pen.setposition(-300, -300)
pen.setposition(-300, -5)
pen.setposition(300, -5)
pen.hideturtle()

# Create a text display for points
t = turtle.Turtle()
t.setposition(150, 150)
pointg = 0

# Function for jumping
jumped = False
def jump():
    global jumped
    if not jumped:
        jumped = True
        player.speed(0)
        player.dy = 30
        player.sety(player.ycor() + player.dy)
        player.speed(pspeed)
        player.forward(70)
        player.sety(player.ycor() - player.dy)
        jumped = False
        player.speed(pspeed)

# Listen for jump input
turtle.listen()
turtle.onkey(jump, "space")

# Main game loop
while True:
    p3.forward(1)
    p2.forward(enemspeed)
    player.forward(pspeed)

    if player.xcor() >= 300:
        player.speed(0)
        player.setposition(player.xcor() * (-1) + 10, player.ycor())
        if pspeed <= 10:
            pspeed += 0.1
            enemspeed += 0.1
        player.speed(pspeed)
        p2.speed(enemspeed)
        pointg += 1
        t.clear()
        t.write(pointg, font=("Arial", 16, "bold"), align="center")

    if player.ycor() >= 300 or player.ycor() <= -300:
        player.speed(0)
        player.setposition(player.xcor(), player.ycor() * (-1))
        if pspeed <= 10:
            pspeed += 0.1
            enemspeed += 0.1
        player.speed(pspeed)
        p2.speed(enemspeed)
        pointg += 1
        t.clear()
        t.write(pointg, font=("Arial", 16, "bold"), align="center")

    if p2.xcor() >= 300 or p2.xcor() <= -300:
        p2.setposition(p2.xcor() * (-1), p2.ycor())
    if p2.ycor() >= 300 or p2.ycor() <= -300:
        p2.setposition(p2.xcor(), p2.ycor() * (-1))

    if p3.xcor() >= 300 or p3.xcor() <= -300:
        p3.speed(0)
        p3.setposition(p3.xcor() * (-1), p3.ycor())
        p3.speed(1)
    if p3.ycor() >= 300 or p3.ycor() <= -300:
        p3.speed(0)
        p2.setposition(p3.xcor(), p3.ycor() * (-1))
        p3.speed(1)

    d2 = math.sqrt((player.xcor() - p2.xcor())**2 + (player.ycor() - p2.ycor())**2)
    d3 = math.sqrt((player.xcor() - p3.xcor())**2 + (player.ycor() - p3.ycor())**2)

    if d2 <= 15 or d3 <= 15:
        t.hideturtle()
        pointg -= 1
        t.clear()
        t.write(pointg, font=("Arial", 16, "bold"), align="center")
        t.hideturtle()
