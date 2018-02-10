#player's tank

import pygame
from pygame.sprite import Sprite
import math

class Player(Sprite):
    def __init__(self, image_bottom, image_top , start_x, start_y, screen):
        super(Player,self).__init__()
        #why do we need super??
        self.image_bottom = pygame.image.load(image_bottom)
        self.image_bottom = pygame.transform.scale(self.image_bottom,(150,150))
        self.image_top = pygame.image.load(image_top)
        self.image_top = pygame.transform.scale(self.image_top,(150, 150))
        
        self.bottom_angle = 45 
        # self.bottom_angle = self.bottom_angle % 360 
        

        self.speed = 30
        self.turn_speed = 5

        self.x = start_x
        self.y = start_y
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, 150, 150)
		

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
        self.rect = pygame.Rect(self.x, self.y, 150, 150)

		
	# 2. The methods where you define all the class functions (methods)
    def draw_me(self):
        copied_image = self.image_bottom.copy()
        copied_image = pygame.transform.rotate(copied_image, self.bottom_angle)
        width = copied_image.get_rect()[2]
        height = copied_image.get_rect()[3]
        change_coo_x = (width - self.rect[2]) / 2
        change_coo_y = (height - self.rect[3]) / 2
        
        
        self.screen.blit(copied_image, [self.x - change_coo_x, self.y - change_coo_y])
        self.screen.blit(self.image_top, [self.x,self.y])

    def turn_left(self):
        self.bottom_angle += self.turn_speed

    def turn_right(self):
        self.bottom_angle -= self.turn_speed

    def move_up(self):
        self.bottom_angle = self.bottom_angle % 360
        if self.bottom_angle >= 0 and self.bottom_angle < 90:
            radians = self.bottom_angle * math.pi / 180
            add_x = math.cos(radians) * self.speed
            add_y = math.sin(radians) * self.speed
            self.x += add_x
            self.y -= add_y
            
        if self.bottom_angle >= 90 and self.bottom_angle < 180:
            radians = (180 - self.bottom_angle) * math.pi / 180
            add_x = math.cos(radians) * self.speed
            add_y = math.sin(radians) * self.speed
            self.x -= add_x
            self.y -= add_y

        if self.bottom_angle >= 180 and self.bottom_angle < 270:
            radians = (self.bottom_angle - 180) * math.pi / 180
            add_x = math.cos(radians) * self.speed
            add_y = math.sin(radians) * self.speed
            self.x -= add_x
            self.y += add_y

        if self.bottom_angle >= 270 and self.bottom_angle < 360:
            radians = (360 - self.bottom_angle ) * math.pi / 180
            add_x = math.cos(radians) * self.speed
            add_y = math.sin(radians) * self.speed
            self.x += add_x
            self.y += add_y
            print math.cos(radians)
        
    
    def move_down(self):
        self.bottom_angle = self.bottom_angle % 360
        speed = self.speed / 2
        if self.bottom_angle >= 0 and self.bottom_angle < 90:
            radians = self.bottom_angle * math.pi / 180
            add_x = math.cos(radians) * speed
            add_y = math.sin(radians) * speed
            self.x -= add_x
            self.y += add_y
            
        if self.bottom_angle >= 90 and self.bottom_angle < 180:
            radians = (180 - self.bottom_angle) * math.pi / 180
            add_x = math.cos(radians) * speed
            add_y = math.sin(radians) * speed
            self.x += add_x
            self.y += add_y

        if self.bottom_angle >= 180 and self.bottom_angle < 270:
            radians = (self.bottom_angle - 180) * math.pi /180
            add_x = math.cos(radians) * speed
            add_y = math.sin(radians) * speed
            self.x += add_x
            self.y -= add_y

        if self.bottom_angle >= 270 and self.bottom_angle < 360:
            radians = (360 - self.bottom_angle ) * math.pi / 180
            add_x = math.cos(radians) * speed
            add_y = math.sin(radians) * speed
            self.x -= add_x
            self.y -= add_y
  

		


	
