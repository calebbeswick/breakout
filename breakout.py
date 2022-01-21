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
BALL_SPEED = 6

# Sets up the colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN =(0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BACKROUND_COLOR = WHITE
PADDLE_COLOR = BLACK
BALL_COLOR = BLACK

pygame.init()
pygame.mixer.init() # add this line
mainsurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
pygame.display.set_caption("Breakout")
mainsurface.fill((BACKROUND_COLOR))

# Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
# the screen (BRICK_Y_OFFSET)

pygame.mixer.music.load('backround_music.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.5)


x_pos = BRICK_SEP
y_pos = BRICK_Y_OFFSET
total = 0
bricks = pygame.sprite.Group()
colors = [RED, ORANGE, YELLOW, GREEN, CYAN]
for color in colors:
    for x in range(2):
        for x in range(BRICKS_PER_ROW):
            b = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
            b.rect.x = x_pos
            b.rect.y = y_pos
            mainsurface.blit(b.image, b.rect)
            bricks.add(b)
            x_pos = x_pos + BRICK_WIDTH + BRICK_SEP

        y_pos += 15
        x_pos = BRICK_SEP
paddle_group = pygame.sprite.Group()
paddle = paddle.Paddle(PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)
paddle_group.add(paddle)
paddle.rect.x = 160
paddle.rect.y = 500

ba = ball.Ball(BALL_COLOR, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
ba.rect.x = APPLICATION_WIDTH / 2
ba.rect.y = APPLICATION_HEIGHT / 2
game_over = False
while True:
    mainsurface.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            paddle.move(pygame.mouse.get_pos())
    mainsurface.blit(ba.image, ba.rect)
    ba.move()
    ba.brick_collide(bricks)
    ba.paddle_collide(paddle_group)
    mainsurface.blit(paddle.image, paddle.rect)
    font = pygame.font.Font(None, 36)
    center = APPLICATION_WIDTH / 2
    for x in bricks:
        mainsurface.blit(x.image, x.rect)
    # if len(bricks) == 100:
    #     game_over = True
    # if game_over:
    #     text = font.render("Game Over", True, WHITE)
    #     textpos = text.get_rect()
    #     textpos.top = 300
    #     mainsurface.blit(text, textpos)


    pygame.display.update()
    time.tick(30)