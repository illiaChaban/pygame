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

        self.top_angle_rad = self.top_angle * math.pi / 180

        
        self.speed = 0
        self.turn_speed = 0

        self.x = start_x
        self.y = start_y

        # self.x_top = 0
        # self.x_top = 0
        self.screen = screen
        self.screen_width = self.screen.get_rect()[2]
        self.screen_height = self.screen.get_rect()[3]

        self.rect = pygame.Rect(self.x, self.y, 72, 38)


        self.cool_down = 1400
        self.last_shot_tick = 0

        self.shell_image = pygame.image.load("images/tank_shell1_cropped.png")
        self.shell_image = pygame.transform.scale(self.shell_image, (10, 50))
        
        
        
	#	
	# 2. The methods where you define all the class functions (methods)
    def draw_me(self):

        self.draw_reload_bar()


        #when the bottom rotates it changes its center, that's why we have to update top-left corner
        # with every rotation. (self.x, self.y) become center of the image
        copied_image = self.image_bottom.copy()
        copied_image = pygame.transform.rotate(copied_image, self.bottom_angle)
        
        change_coo_x = copied_image.get_rect().center[0] 
        change_coo_y = copied_image.get_rect().center[1]
        self.screen.blit(copied_image, [self.x - change_coo_x, self.y - change_coo_y])

        # self.rect = pygame.transform.rotate(self.rect, self.bottom_angle)
        # print self.rect

        #################################
        # top image rotates relative to mouse position
        x2 = pygame.mouse.get_pos()[0]
        y2 = pygame.mouse.get_pos()[1]

        #finding angle between mouse and tank
        dx = x2 - self.x 
        dy = y2 - self.y 
        rads = math.atan2(-dy, dx) #% (2* math.pi)
        angle = math.degrees(rads)
        self.top_angle = angle
        
        # print 'tank ' + str(self.x) + ' : ' + str(self.y)
        # print pygame.mouse.get_pos()
        

        #changes the relative center of image_top
        radians_top = self.top_angle * math.pi / 180
        change_x = math.cos(radians_top) * (20)   
        change_y = math.sin(radians_top) * (-20)

        # changing the top-left corner while rotating, self.x / y become center of the image
        copied_top = self.image_top.copy()
        copied_top = pygame.transform.rotate(copied_top, self.top_angle)
        change_coo_x_top = copied_top.get_rect().center[0] 
        change_coo_y_top = copied_top.get_rect().center[1] 

        # self.x_top = self.x - change_coo_x_top + change_x
        # self.y_top = self.y - change_coo_y_top + change_y 
        
        self.screen.blit(copied_top, [self.x - change_coo_x_top + change_x , self.y - change_coo_y_top + change_y ])

    def turn_left(self):
        self.turn_speed = 5
        

    def turn_right(self):
        self.turn_speed = -5
        

    def move_up(self):
        self.speed = 6
    
    def move_down(self):
        self.speed = - 3

    def stop(self):
        self.speed = 0

    def stop_turn(self):
        self.turn_speed = 0         

    def update(self):
        # if self.x > 600:             #set up the boundaries of the screen
        #     self.x = 600
        # if self.x < 100:
        #     self.x = 100
        # if self.y > 500:
        #     self.y = 500
        # if self.y < 50:
        #     self.y = 50

        # print self.x_top
        radians = self.bottom_angle * math.pi / 180
        add_x = math.cos(radians) * self.speed
        add_y = math.sin(radians) * self.speed
        self.x += add_x
        self.y -= add_y

        self.bottom_angle += self.turn_speed

    def draw_reload_bar(self):

        reload0 = pygame.image.load("images/reload_bar01.png")
        reload0 = pygame.transform.scale( reload0, (10,50))

        reload1 = pygame.image.load("images/reload_bar11.png")
        reload1 = pygame.transform.scale( reload1, (10,50))

        reload2 = pygame.image.load("images/reload_bar21.png")
        reload2 = pygame.transform.scale( reload2, (10,50))

        reload3 = pygame.image.load("images/reload_bar31.png")
        reload3 = pygame.transform.scale( reload3, (10,50))

        current_tick = pygame.time.get_ticks()

        

        if current_tick - self.last_shot_tick < self.cool_down / 4:
            self.screen.blit(reload0, [self.screen_width - 20, self.screen_height - 60])
        elif current_tick - self.last_shot_tick < self.cool_down / 4 * 2:
            self.screen.blit(reload1, [self.screen_width - 20, self.screen_height - 60])
        elif current_tick - self.last_shot_tick < self.cool_down / 4 * 3:
            self.screen.blit(reload2, [self.screen_width - 20, self.screen_height - 60])
        elif current_tick - self.last_shot_tick < self.cool_down:
            self.screen.blit(reload3, [self.screen_width - 20, self.screen_height - 60])
        else:
            self.screen.blit(self.shell_image, [self.screen_width - 20, self.screen_height - 60])


        

    

   

  

		


	
