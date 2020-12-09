import turtle, time

WIDTH = 800
HEIGHT = 600

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
paddle_a.goto(-(WIDTH / 2 - 32), 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto((WIDTH / 2 - 32), 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Bindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > (HEIGHT / 2 - 16):
        ball.sety(HEIGHT / 2 - 16)
        ball.dy *= -1
    elif ball.ycor() < ((- HEIGHT) / 2 + 16):
        ball.sety((- HEIGHT) / 2 + 16)
        ball.dy *= -1

    if ball.xcor() > (WIDTH / 2 - 16):
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < ((- WIDTH) / 2 + 16):
        ball.goto(0, 0)
        ball.dx *= -1

    # Collisions Checking
    if ball.xcor() > (WIDTH / 2 - 32) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(WIDTH / 2 - 32)
        ball.dx *= -1
    
    if ball.xcor() < -(WIDTH / 2 - 32) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-(WIDTH / 2 - 32))
        ball.dx *= -1

    time.sleep(1 / 60)