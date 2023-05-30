
import turtle
import random
import math
import time
#okno
window = turtle.Screen()
window.bgcolor("lightgreen")

#create player
player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
#disable the trail
player.penup()
#don't pause when changing directions
player.speed(0)
pspeed = 1
player.speed(pspeed)
enemspeed = 1

#point
# point = turtle.Turtle()
# point.shape("circle")
# point.color("yellow")
# point.penup()
# point.speed(0)
# point.setposition(random.randint(-250, 250), random.randint(-250, 250))
p2 = turtle.Turtle()
p2.shape("triangle")
p2.color("red")
p2.penup()

p2.setposition(220, 0)
p2.left(180)

#disable the trail
#don't pause when changing directions
p2.speed(10)

p3 = turtle.Turtle()
p3.shape("triangle")
p3.color("red")
p3.penup()

p3.setposition(p2.xcor() + 50, 0)
p3.left(180)

p3.speed(5)




#draw border
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.setposition(-300, -300)
pen.pendown()
#change pen size
pen.pensize(5)
pen.setposition(300, -300)
pen.setposition(300, 300)
pen.setposition(-300, 300)
pen.setposition(-300, -300)
pen.setposition(-300, -5)
pen.setposition(300, -5)




#hide object



pen.hideturtle()
pen.penup()
t = turtle.Turtle()
t.setposition(150, 150)
pointg = 0

t.write(pointg, font=("Arial", 16, "bold"), align="center")
t.clear()
t.write(pointg, font=("Arial", 16, "bold"), align="center")

t.hideturtle()


#functions
jumped = False
def jump():
    global jumped
    if jumped == False:
        jumped = True
        player.speed(0)
        player.dy = 30
        
        player.sety(player.ycor() + player.dy)
        player.speed(pspeed)

        player.forward(70)
        player.sety(player.ycor() - player.dy)
        jumped = False
        player.speed(pspeed)







    
    

#listen to our inputs
turtle.listen()
turtle.onkey(jump, "space")
    

while True:
    
    p3.forward(1)
    p2.forward(enemspeed)


    player.forward(pspeed)
    if player.xcor() >= 300 :
        player.speed(0)
        player.setposition(player.xcor()*(-1)+ 10, player.ycor())
        if pspeed <=10:
            pspeed += 0.1
            enemspeed += 0.1

        player.speed(pspeed)
        p2.speed(enemspeed)

        pointg += 1
        t.clear()


        

        t.write(pointg, font=("Arial", 16, "bold"), align="center")
    if player.ycor() >= 300 or player.ycor() <= -300:
        player.speed(0)

        player.setposition(player.xcor(), player.ycor()*(-1))
        if pspeed <=10:
            pspeed += 0.1
            enemspeed += 0.1

        player.speed(pspeed)
        p2.speed(enemspeed)

        pointg += 1
        t.clear()

        

        t.write(pointg, font=("Arial", 16, "bold"), align="center")
        
    #wad
    if p2.xcor() >= 300 or p2.xcor() <= -300:
        p2.setposition(p2.xcor()*(-1), p2.ycor())
    if p2.ycor() >= 300 or p2.ycor() <= -300:
        p2.setposition(p2.xcor(), p2.ycor()*(-1))
    

    if p3.xcor() >= 300 or p3.xcor() <= -300:
        p3.speed(0)
        p3.setposition(p3.xcor()*(-1), p3.ycor())
        p3.speed(1)
    if p3.ycor() >= 300 or p3.ycor() <= -300:
        p3.speed(0)

        p2.setposition(p3.xcor(), p3.ycor()*(-1))
        p3.speed(1)



    # if point.xcor() - player.xcor() <= 5 and point.ycor() - player.ycor() <= 5:
    #     point.setposition(random.randint(-250, 250), random.randint(-250, 250))
    # d = math.sqrt((player.xcor() - point.xcor())**2 + (player.ycor() - point.ycor())**2)
    # if d <=15:
    #     pointg +=1
    #     point.setposition(random.randint(-250, 250), random.randint(-250, 250))
    #     t.setposition(150, 150)
    #     t.hideturtle()
    #     
    #przeszkadza
    d2 = math.sqrt((player.xcor() - p2.xcor())**2 + (player.ycor() - p2.ycor())**2)
    d3 = math.sqrt((player.xcor() - p3.xcor())**2 + (player.ycor() - p3.ycor())**2)

    if d2 <=15 or d3 <=15:
        t.hideturtle()
        pointg -=1
        t.clear()

        

        t.write(pointg, font=("Arial", 16, "bold"), align="center")
        t.hideturtle()



