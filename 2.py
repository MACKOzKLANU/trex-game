import turtle

# Set up the screen
wn = turtle.Screen()
wn.setup(width=600, height=400)

# Create the player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("black")
player.penup()
player.goto(-250, 0)
player.dy = 0
player.right(90)

# Define the jump function
def jump():
    player.dy = 10

# Set up the keyboard bindings
wn.listen()
wn.onkeypress(jump, "space")

# Set up the game loop
while True:
    player.speed(1)
    # Move the player
    player.dy -= 0.5
    player.sety(player.ycor() + player.dy)

    # Check for collision with ground
    if player.ycor() < -180:
        player.dy = 0
        player.sety(-180)

    wn.update()

# Exit the game
wn.mainloop()
