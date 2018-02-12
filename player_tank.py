#player's tank

import pygame
from pygame.sprite import Sprite
import math

class Player(Sprite):
    def __init__(self, image_bottom, image_top , start_x, start_y, screen):
        super(Player,self).__init__()
        #why do we need super??
        self.image_bottom = pygame.image.load(image_bottom)
        self.image_bottom = pygame.transform.scale(self.image_bottom,(74,38))
        self.image_top = pygame.image.load(image_top)
        self.image_top = pygame.transform.scale(self.image_top,(72, 28))
        
        self.bottom_angle = 0 
        self.top_angle = 0

        
        self.speed = 6
        self.speed_x = 0
        self.speed_y = 0
        self.turn_speed = 0

        self.x = start_x
        self.y = start_y
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, 70, 70)
        self.shell1 = pygame.image.load("images/tank_shell1_cropped.png")
        self.shell1 = pygame.transform.scale(self.shell1, (20,20))
		

    def update_me(self,player_pos): ## wtf i'm doing here????
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

	#	
	# 2. The methods where you define all the class functions (methods)
    def draw_me(self):
        #when the bottom rotates it changes its center, that's why we have to update the center while we rotate
        copied_image = self.image_bottom.copy()
        copied_image = pygame.transform.rotate(copied_image, self.bottom_angle)
        width = copied_image.get_rect()[2]
        height = copied_image.get_rect()[3]
        change_coo_x = (width - self.rect[2]) / 2
        change_coo_y = (height - self.rect[3]) / 2
        self.screen.blit(copied_image, [self.x - change_coo_x, self.y - change_coo_y])

        # top_image should remain in the center of the vehicle while it rotates.
        #it should change its position too
       
        
        #changes the relative center of image_top
        radians_top = self.top_angle * math.pi / 180
        change_x = math.cos(radians_top) * (-15)   #8 pixels - how far back i want to put the tank top
        change_y = math.sin(radians_top) * (-15)
        #optimize
        x2 = pygame.mouse.get_pos()[0]
        y2 = pygame.mouse.get_pos()[1]
        centered_x = self.image_top.get_rect().center[0] 
        centered_y = self.image_top.get_rect().center[1]

        #finding angle between mouse and tank
        dx = x2 - self.x - centered_x + change_x
        dy = y2 - self.y - centered_y + change_y
        rads = math.atan2(-dy, dx) % (2* math.pi)
        angle = math.degrees(rads)
        self.top_angle = angle

        # changing the center while rotating 
        copied_top = self.image_top.copy()
        copied_top = pygame.transform.rotate(copied_top, self.top_angle)
        width_top = copied_top.get_rect()[2]
        height_top = copied_top.get_rect()[3]
        change_coo_x_top = (width_top - self.rect[2]) / 2
        change_coo_y_top = (height_top - self.rect[3]) / 2
        
        
        # print self.image_top.get_rect().center
        self.screen.blit(copied_top, [self.x - change_x - change_coo_x_top,self.y  + change_y - change_coo_y_top])

    def turn_left(self):
        self.turn_speed = 5
        

    def turn_right(self):
        self.turn_speed = -5
        

    def move_up(self):
        radians = self.bottom_angle * math.pi / 180
        add_x = math.cos(radians) * self.speed
        add_y = math.sin(radians) * self.speed
        self.speed_x = add_x
        self.speed_y = - add_y
            
        
    
    def move_down(self):
        speed = self.speed / 2
        radians = self.bottom_angle * math.pi / 180
        add_x = math.cos(radians) * speed
        add_y = math.sin(radians) * speed
        self.speed_x = - add_x
        self.speed_y = add_y

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0

    def stop_turn(self):
        self.turn_speed = 0         

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.bottom_angle += self.turn_speed

    def shoot(self):
        shell_speed = 40
        #check top_angle
        start_x = self.x
        start_y = self.y
        end_x = pygame.mouse.get_pos()[0]
        end_y = pygame.mouse.get_pos()[1]
        print start_x
        self.top_angle 

    

   

  

		


	
