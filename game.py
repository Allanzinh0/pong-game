import turtle

WIDTH = 640
HEIGHT = 480

# Initialize the window
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=WIDTH, height=HEIGHT)
window.tracer(0)

# Main game loop
while True:
    window.update()