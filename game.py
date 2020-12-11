import pygame
from pygame.locals import *
from OpenGL.GL import *

# Global Variables
WIDTH = 640
HEIGHT = 480

# Ball Variables
xBall = 0
dxBall = 3
yBall = 0
dyBall = 3
ballSize = 16

# Player Variables
yPlayer1 = 0
yPlayer2 = 0
playerSpeed = 10

def playerWidth():
    return ballSize

def playerHeight():
    return ballSize * 4

def xPlayer1():
    return playerWidth() * 1.5 - WIDTH / 2

def xPlayer2():
    return WIDTH / 2 - playerWidth() * 1.5

# Initialize Window
pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
sndBounce = pygame.mixer.Sound("assets/bounce.wav")

def drawRect(x, y, dx, dy, r, g, b):
    glColor3f(r, g, b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * dx + x, -0.5 * dy + y)
    glVertex2f(0.5 * dx + x, -0.5 * dy + y)
    glVertex2f(0.5 * dx + x, 0.5 * dy + y)
    glVertex2f(-0.5 * dx + x, 0.5 * dy + y)
    glEnd()

def updateFrame():
    global xBall, yBall, dxBall, dyBall, yPlayer1, yPlayer2

    # Ball Movement
    xBall += dxBall
    yBall += dyBall

    if (xBall - ballSize / 2 < xPlayer1() + playerWidth() / 2
    and yBall - ballSize / 2 < yPlayer1 + playerHeight() / 2
    and yBall + ballSize / 2 > yPlayer1 - playerHeight() / 2):
        dxBall *= -1
        sndBounce.play()

    if (xBall + ballSize / 2 > xPlayer2() - playerWidth() / 2
    and yBall - ballSize / 2 < yPlayer2 + playerHeight() / 2
    and yBall + ballSize / 2 > yPlayer2 - playerHeight() / 2):
        dxBall *= -1
        sndBounce.play()

    if xBall + ballSize / 2 > WIDTH / 2 or xBall - ballSize / 2 < - WIDTH / 2:
        dxBall *= -1
        xBall = 0
        yBall = 0

    if yBall + ballSize / 2 > HEIGHT / 2 or yBall - ballSize / 2 < - HEIGHT / 2:
        dyBall *= -1
        sndBounce.play()

    # Get Keyboard Input
    keys = pygame.key.get_pressed()

    # Player 1 Movement
    if keys[K_w]:
        yPlayer1 += playerSpeed

        if (yPlayer1 > HEIGHT / 2 - playerHeight() / 2):
            yPlayer1 = HEIGHT / 2 - playerHeight() / 2

    if keys[K_s]:
        yPlayer1 -= playerSpeed

        if (yPlayer1 < playerHeight() / 2 - HEIGHT / 2):
            yPlayer1 = playerHeight() / 2 - HEIGHT / 2

    # Player 2 Movement
    if keys[K_UP]:
        yPlayer2 += playerSpeed

        if (yPlayer2 > HEIGHT / 2 - playerHeight() / 2):
            yPlayer2 = HEIGHT / 2 - playerHeight() / 2

    if keys[K_DOWN]:
        yPlayer2 -= playerSpeed

        if (yPlayer2 < playerHeight() / 2 - HEIGHT / 2):
            yPlayer2 = playerHeight() / 2 - HEIGHT / 2


def drawFrame():
    glViewport(0, 0, WIDTH, HEIGHT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-WIDTH / 2, WIDTH / 2, - HEIGHT / 2, HEIGHT / 2, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    drawRect(xBall, yBall, ballSize, ballSize, 1, 1, 0)
    drawRect(xPlayer1(), yPlayer1, playerWidth(), playerHeight(), 1, 0, 0)
    drawRect(xPlayer2(), yPlayer2, playerWidth(), playerHeight(), 0, 0, 1)

    pygame.display.flip()

while True:
    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    updateFrame()
    drawFrame()
