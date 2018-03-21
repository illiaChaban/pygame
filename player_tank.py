import pygame
from pygame.sprite import Sprite
import math

class Player(Sprite):
    def __init__(self, image_bottom, image_top , start_x, start_y, screen):
        super(Player,self).__init__()
        self.image_bottom = pygame.image.load(image_bottom)
        self.image_bottom = pygame.transform.scale(self.image_bottom,(74,38))

        self.width = self.image_bottom.get_rect()[2]  ### the image has some transparent space at the back
        self.height = self.image_bottom.get_rect()[3]

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

        self.cornersList = self.find_corners(self.bottom_angle, self.x, self.y, self.width, self.height)
        

    def draw_me(self):

        self.draw_reload_bar()
        self.draw_bottom()
        self.draw_top()

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

    def update(self, list_of_objects):

        self.move_tank_bottom(list_of_objects)
        self.map_wall_restrictions()
        self.top_angle = self.find_mouse_angle()

        self.cornersList = self.find_corners(self.bottom_angle, self.x, self.y, self.width, self.height)


    def move_tank_bottom(self, list_of_objects):
        radians = self.bottom_angle * math.pi / 180
        add_x = math.cos(radians) * self.speed
        add_y = math.sin(radians) * self.speed

        new_bottom_angle = self.bottom_angle + self.turn_speed 
        new_x = self.x + add_x
        new_y = self.y - add_y

        if self.detect_collision(list_of_objects, self.find_corners(new_bottom_angle, new_x, new_y, self.width, self.height)):
            new_x = self.x + add_x/2 
            new_y = self.y - add_y/2
            new_bottom_angle = self.bottom_angle + self.turn_speed/2
        if not self.detect_collision(list_of_objects, self.find_corners(new_bottom_angle, self.x, self.y, self.width, self.height) ):
            self.bottom_angle = new_bottom_angle
        if not self.detect_collision(list_of_objects, self.find_corners(self.bottom_angle, new_x, self.y, self.width, self.height) ):
            self.x = new_x
        if not self.detect_collision(list_of_objects, self.find_corners(self.bottom_angle, self.x, new_y, self.width, self.height) ):
            self.y = new_y


    def map_wall_restrictions(self):
        width = self.screen.get_rect()[2]
        height = self.screen.get_rect()[3]
        offset = 40
        if self.x > width - offset:             #set up the boundaries of the screen
            self.x = width - offset
        if self.x < offset:
            self.x = offset
        if self.y > height - offset:
            self.y = height - offset
        if self.y < offset:
            self.y = offset
        
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

    def find_corners(self, angle, center_x, center_y, width, height):
        #x1,y1###############x2,y2#
        #                         #
        #                         #
        #x4,y4###############x3,y3#

        corners_list = [[0,0] for x in range(4)]
        #pretend points when angle is 0 = points about [self.x, self.y] as center
        # ( vectors and stuff )  - self.x / - self.y
        for i in range(len(corners_list)):  ## the image has some transparent space at its left
            if i > 1:
                y_p = height /2
            else: 
                y_p = - height / 2
            if i == 1 or i == 2:
                x_p = width / 2
            else: 
                x_p = - width / 2 + 10
            corners_list[i][0] = self.find_rotated_x([x_p, y_p], angle, center_x)
            corners_list[i][1] = self.find_rotated_y([x_p, y_p], angle, center_y)
        return corners_list

    def find_rotated_x(self, pretend_point_coordinates, angle, center_x):
        radians = angle * math.pi / 180
        x = pretend_point_coordinates[0]
        y = pretend_point_coordinates[1]
        return x * math.cos(radians) + y * math.sin(radians) + center_x 

    def find_rotated_y(self, pretend_point_coordinates, angle, center_y):
        radians = angle * math.pi / 180
        x = pretend_point_coordinates[0]
        y = pretend_point_coordinates[1]
        return y * math.cos(radians) - x * math.sin(radians) + center_y 

    def point_within_my_area(self, point_coordinates, corners_list):
        #x1,y1###############x2,y2#
        #                         #
        #                         #
        #x4,y4###############x3,y3#

        ## straight (line) formula =>  ax + bx + c = 0  
        ##  or   (y1 -y2)x + (x2 - x1)y + (x1y2 - x2y1) = 0
        x = point_coordinates[0]
        y = point_coordinates[1]

        for i in range(len(corners_list)):
            x1 = corners_list[i][0]
            y1 = corners_list[i][1]

            next_i = (i + 1) % (len(corners_list))
            x2 = corners_list[next_i][0]
            y2 = corners_list[next_i][1]

            a = y1 - y2
            b = x2 - x1
            c = x1 * y2 - x2 * y1

            if a * x + b * y + c < 0:  ## checking if the point lies on the right side 
                return False           ## of every line, which would mean it's inside
        return True                    ## the area

    def detect_collision(self, list_of_objects, my_corners_list):
        for obj in list_of_objects:
            if obj != self:
                if self.it_within_my_area(obj, my_corners_list) or self.me_within_its_area(obj, my_corners_list ):
                    return True
        return False
        
    def it_within_my_area(self, player, my_corners_list):
        for corner in player.cornersList:
            if self.point_within_my_area(corner, my_corners_list):
                return True
        return False

    def me_within_its_area(self, player, cornersList):
        if player != self:
            for corner in cornersList:
                if player.point_within_my_area(corner):
                    return True
        return False


	
