import pygame, sys
from pygame.locals import *
import brick, paddle, ball

time = pygame.time.Clock()

# Constants that will be used in the program
APPLICATION_WIDTH = 400
APPLICATION_HEIGHT = 600
PADDLE_Y_OFFSET = 30
BRICKS_PER_ROW = 10
BRICK_SEP = 4  # The space between each brick
BRICK_Y_OFFSET = 70
BRICK_WIDTH = int((APPLICATION_WIDTH - (BRICKS_PER_ROW * BRICK_SEP)) / BRICKS_PER_ROW)
BRICK_HEIGHT = 8
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10
RADIUS_OF_BALL = 10
NUM_TURNS = 3

# Sets up the colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN =(0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.font.init()
pygame.mixer.init()
mainsurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
pygame.display.set_caption("Breakout")
mainsurface.fill((255, 255, 255))

# Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
# the screen (BRICK_Y_OFFSET)

x_pos = BRICK_SEP
y_pos = BRICK_Y_OFFSET
total = 0
bricks = pygame.sprite.Group()
for x in range(10):
    for x in range(10):
        for x in range(BRICKS_PER_ROW):
            if total <= 1:
                color = RED
                speed = 10
            elif total >=2 and total <= 3:
                color = ORANGE
                speed = 9
            elif total >=4 and total <=5:
                color = YELLOW
                speed = 8
            elif total >=6 and total <= 7:
                color = GREEN
                speed = 7
            elif total >=8 and total <= 9:
                color = CYAN
                speed = 6
            b = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
            bricks.add(b)
            b.rect.x = x_pos
            b.rect.y = y_pos
            mainsurface.blit(b.image, b.rect)
            x_pos = x_pos + BRICK_WIDTH + BRICK_SEP
    y_pos = y_pos + 15
    x_pos = BRICK_SEP
    total = total + 1

paddle_group = pygame.sprite.Group()
paddle = paddle.Paddle(PADDLE_WIDTH, PADDLE_HEIGHT, BLACK)
paddle_group.add(paddle)
paddle.rect.x = 160
paddle.rect.y = 500

ba = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
ba.rect.x = APPLICATION_WIDTH / 2
ba.rect.y = APPLICATION_HEIGHT / 2

while True:
    mainsurface.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            paddle.move(pygame.mouse.get_pos())
    length = len(bricks)
    ba.move(length)
    ba.paddle_collide(paddle_group)
    ba.brick_collide(bricks)
    mainsurface.blit(ba.image, ba.rect)
    mainsurface.blit(paddle.image, paddle.rect)

    for x in bricks:
        mainsurface.blit(x.image, x.rect)



    pygame.display.update()
    time.tick(30)