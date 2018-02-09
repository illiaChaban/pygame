#player's tank

import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, image_bottom, image_top , start_x, start_y, screen):
        super(Player,self).__init__()
        #why do we need super??
        self.image_bottom = pygame.image.load(image_bottom)
        self.image_bottom = pygame.transform.scale(self.image_bottom,(150,150))
        self.image_top = pygame.image.load(image_top)
        self.image_top = pygame.transform.scale(self.image_top,(150, 150))
        
        self.bottom_angle = 0

        self.x = start_x
        self.y = start_y
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, 300, 300)
		

    def update_me(self,player_pos):
        self.x = player_pos[0]
        self.y = player_pos[1]
        if self.x > 690:             #set up the boundaries of the ship
            self.x = 690
        elif self.x < 10:
            self.x = 10
        elif self.y > 690:
            self.y = 690
        elif self.y < 10:
            self.y = 10
        else:
            self.x = player_pos[0]
            self.y = player_pos[1]
        self.rect = pygame.Rect(self.x, self.y, 70, 70)

		
	# 2. The methods where you define all the class functions (methods)
    def draw_me(self):
        copied_image_bottom = self.image_bottom.copy()
        pygame.transform.rotate(copied_image_bottom, self.bottom_angle)
        self.screen.blit(self.image_bottom, [self.x,self.y])
        # self.screen.blit(self.image_top, [self.x,self.y])

		


	
