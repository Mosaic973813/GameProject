import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y): # this initializes the parameters
        super().__init__(x, y, SHOT_RADIUS) # We include the constants of shot radius and color to the calling of the parent class

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        # Remove if off-screen
        # if (self.x < 0 or self.x > SCREEN_WIDTH or
        #     self.y < 0 or self.y > SCREEN_HEIGHT):
        #     self.kill()