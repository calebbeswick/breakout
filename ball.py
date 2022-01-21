import pygame
import brick
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface(((radius * 2), (radius * 2)))
        self.image.fill((255, 255, 255))





        # Add a circle to represent the ball to the surface just created. Just use the pygame.draw.circle method.
        # The surface will be self.image
        pygame.draw.circle(self.image, (self.color), (10, 10), self.radius)
        self.rect = self.image.get_rect()



        # Give the ball an initial speed. You will need a speed for the x direction and one for the y direction.
        self.x_speed = 6
        self.y_speed = 6




    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.left < 0 or self.rect.right > self.windowWidth:
            self.x_speed = -self.x_speed
        if self.rect.top < 0 or self.rect.bottom > self.windowHeight:
            self.y_speed = -self.y_speed
        # if self.rect.bottom > self.windowHeight:
        #     self.y_speed = 0
        #     self.x_speed = 0







    def paddle_collide(self, group):
        if pygame.sprite.spritecollide(self, group, False):
            self.y_speed = -self.y_speed


    def brick_collide(self, group):
        length = len(group)
        if pygame.sprite.spritecollide(self, group, True):
            self.y_speed = -self.y_speed
            speed = 17
            if length >= 90:
                speed = 7
            elif length >= 80:
                speed = 9
            elif length >= 70:
                speed = 11
            elif length >= 60:
                speed = 13
            elif length >= 50:
                speed = 15
            self.y_speed = speed
