import pygame
from pygame.sprite import Sprite
import math

class Player(Sprite):
    def __init__(self, image_bottom, image_top , start_x, start_y, screen):
        super(Player,self).__init__()
        self.image_bottom = pygame.image.load(image_bottom)
        self.image_bottom = pygame.transform.scale(self.image_bottom,(74,38))

        self.image_top = pygame.image.load(image_top)
        self.image_top = pygame.transform.scale(self.image_top,(72, 28))
        
        self.bottom_angle = 0 
        self.top_angle = 0
        
        self.speed = 0
        self.turn_speed = 0

        self.x = start_x
        self.y = start_y

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
        self.draw_bottom()
        self.draw_top()

        # self.rect = pygame.transform.rotate(self.rect, self.bottom_angle)
        # print self.rect

        #################################
        

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

        # moving forward
        radians = self.bottom_angle * math.pi / 180
        add_x = math.cos(radians) * self.speed
        add_y = math.sin(radians) * self.speed
        self.x += add_x
        self.y -= add_y

        self.bottom_angle += self.turn_speed

        self.top_angle = self.find_mouse_angle()

   
    def draw_reload_bar(self):

        reload0 = pygame.image.load("images/reload_bar01.png")
        reload0 = pygame.transform.scale( reload0, (10,50))

        reload1 = pygame.image.load("images/reload_bar11.png")
        reload1 = pygame.transform.scale( reload1, (10,50))

        reload2 = pygame.image.load("images/reload_bar21.png")
        reload2 = pygame.transform.scale( reload2, (10,50))

        reload3 = pygame.image.load("images/reload_bar311.png")
        reload3 = pygame.transform.scale( reload3, (10,50))

        current_tick = pygame.time.get_ticks()

        #reload bar changes image depending on a time passed since last shot

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


    def draw_bottom(self):
        #when the bottom rotates it changes its center, that's why we have to update top-left corner
        # with every rotation. (self.x, self.y) become center of the image
        copied_image = self.image_bottom.copy()
        copied_image = pygame.transform.rotate(copied_image, self.bottom_angle)
        
        change_coo_x = copied_image.get_rect().center[0] 
        change_coo_y = copied_image.get_rect().center[1]
        self.screen.blit(copied_image, [self.x - change_coo_x, self.y - change_coo_y])

   
    def draw_top(self):
        rads = self.find_mouse_angle_rad()
        
        #changes the relative center of image_top
        change_x = math.cos(rads) * (20)   
        change_y = math.sin(rads) * (-20)

        # changing the top-left corner while rotating, self.x / y become center of the image
        copied_top = self.image_top.copy()
        copied_top = pygame.transform.rotate(copied_top, self.top_angle)
        change_coo_x_top = copied_top.get_rect().center[0] 
        change_coo_y_top = copied_top.get_rect().center[1] 
        
        self.screen.blit(copied_top, [self.x - change_coo_x_top + change_x , self.y - change_coo_y_top + change_y ])

    
    def find_mouse_angle_rad(self):
        # top image rotates relative to mouse position
        x2 = pygame.mouse.get_pos()[0]
        y2 = pygame.mouse.get_pos()[1]

        #finding angle between mouse and tank
        dx = x2 - self.x 
        dy = y2 - self.y 
        radians = math.atan2(-dy, dx)
        return radians

    
    def find_mouse_angle(self):
        rads = self.find_mouse_angle_rad()
        return math.degrees(rads)


    

   

  

		


	
