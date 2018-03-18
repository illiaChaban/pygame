#collision
import pygame
from pygame.sprite import Sprite

class Block(Sprite):
    def __init__(self, x, y, color, width, height, screen):
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.image_red = pygame.Surface([width, height])
        self.image_red.fill((255, 0, 0))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.screen = screen   
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def detect_collision(self, area):
        if (False):
            return True
        return False

    def render(self):
        if (self.detect_collision()):
            self.screen.blit(self.image_red, [self.x, self.y])
        else: self.screen.blit(self.image, [self.x, self.y])

    
        

