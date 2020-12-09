import turtle

WIDTH = 640
HEIGHT = 480

# Initialize the window
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=WIDTH, height=HEIGHT)
window.tracer(0)

# Game Objects
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-288, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(288, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Main game loop
while True:
    window.update()