#tank_shells
import pygame
import math
from pygame.sprite import Sprite
clock = pygame.time.Clock()



class Shell(Sprite):
    def __init__(self, image, screen, player): #, mouse_pos):
        super(Shell, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (15,15))

        self.screen = screen
        self.speed = 20
        
        self.angle = player.top_angle
        self.angle_rad = self.angle * math.pi / 180

        self.shot_length = 0
        self.shot_length_current = 0

        self.start_x = player.x + math.cos(self.angle_rad)* 50 #_top
        self.start_y = player.y - math.sin(self.angle_rad)* 50 #_top

        self.x = self.start_x  
        self.y = self.start_y 
        
        self.mouse_pos = pygame.mouse.get_pos()
        
        self.load_scaled_fires()
        self.load_scaled_explosions()

        self.shot_start_tick = pygame.time.get_ticks()
        self.shot_end_tick = 0
        
        
    def draw_shot(self):
        self.draw_fire()
        if self.shot_length - self.shot_length_current == 0:
            self.draw_explosion()
        else: 
            self.draw_bullet()


    def update(self, player):

        x2 = self.mouse_pos[0]
        y2 = self.mouse_pos[1]
        
        # self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.shot_length = math.sqrt((x2 - self.start_x)**2 +(y2 - self.start_y)**2)
        self.shot_length_current = math.sqrt((self.x - self.start_x)**2 + (self.y - self.start_y)**2)
        
        if (self.shot_length - self.shot_length_current) < self.speed:
            self.x = x2
            self.y = y2
            
            #i can put it beyond the screen instead
        elif self.shot_length > self.shot_length_current:
            
            self.x += self.speed * math.cos(self.angle_rad)
            self.y -= self.speed * math.sin(self.angle_rad)
            # self.y -= math.sqrt((self.speed ** 2) - (self.speed * math.cos(angle_radians))**2)
            
            # print self.x, start_x

            ## change self.x, y like top_image
        # else:
        #     self.x = x2
        #     self.y = y2
        #     print "stopped shooting"
        #     ##add explosion
        #     return
        
        #update last tick
        if self.shot_length - self.shot_length_current > 0:
            self.shot_end_tick = pygame.time.get_ticks()



    def load_scaled_fires(self):
        self.fire0 = self.load_scale("images/tank_fire01.png", (30,30))
        self.fire1 = self.load_scale("images/tank_fire11.png", (30,30))
        self.fire2 = self.load_scale("images/tank_fire21.png", (30,30))

    def load_scaled_explosions(self):   
        self.explosion0 = self.load_scale("images/explosion0.png", (60,60))
        self.explosion1 = self.load_scale("images/explosion1.png", (60,60))
        self.explosion2 = self.load_scale("images/explosion2.png", (60,60))
        self.explosion3 = self.load_scale("images/explosion3.png", (60,60))
        self.explosion4 = self.load_scale("images/explosion4.png", (60,60))

    
    def load_scale(self, image_address, scale_tuple):
        loaded_image = pygame.image.load(image_address)
        scaled_image = pygame.transform.scale(loaded_image, scale_tuple)
        return scaled_image
        

    def copy_rotate(self, image, angle):
        copied_image = image.copy()
        copied_image = pygame.transform.rotate(copied_image, angle)
        return copied_image
    
    def draw_fire(self):
        copied_fire0 = self.copy_rotate(self.fire0, self.angle)
        copied_fire1 = self.copy_rotate(self.fire1, self.angle)
        copied_fire2 = self.copy_rotate(self.fire2, self.angle)

        change_x0 = copied_fire0.get_rect().center[0]
        change_y0 = copied_fire0.get_rect().center[1]

        change_x1 = copied_fire1.get_rect().center[0]
        change_y1 = copied_fire1.get_rect().center[1]

        change_x2 = copied_fire2.get_rect().center[0]
        change_y2 = copied_fire2.get_rect().center[1]

        far_from_center_x = math.cos(self.angle_rad) * 15
        far_from_center_y = - math.sin(self.angle_rad) * 15
       
        if (self.shot_length > 80):
            if self.shot_length_current < 23:
                self.screen.blit(copied_fire0, [self.start_x - change_x0 + far_from_center_x, self.start_y - change_y0 + far_from_center_y])
            elif self.shot_length_current < 63:
                self.screen.blit(copied_fire1, [self.start_x - change_x1 + far_from_center_x, self.start_y - change_y1  + far_from_center_y])
            elif self.shot_length_current < 80:
                self.screen.blit( copied_fire1, [self.start_x - change_x2 + far_from_center_x, self.start_y - change_y2  + far_from_center_y])
        
        elif self.shot_length > 25:
            if self.shot_length_current < 20:
                self.screen.blit(copied_fire1, [self.start_x - change_x1 + far_from_center_x, self.start_y - change_y1  + far_from_center_y])
            elif self.shot_length_current < 25:
                self.screen.blit(copied_fire2, [self.start_x - change_x2 + far_from_center_x, self.start_y - change_y2 + far_from_center_y] )

    def draw_explosion(self):
        #recentering
        change_coo = self.explosion0.get_rect().center[0]
        
        current_tick = pygame.time.get_ticks()

        if current_tick - self.shot_end_tick < 60:
            self.screen.blit(self.explosion0, [self.x - change_coo, self.y - change_coo])
        elif current_tick - self.shot_end_tick < 130:
            self.screen.blit(self.explosion1, [self.x - change_coo, self.y - change_coo])
        elif current_tick - self.shot_end_tick < 200:
            self.screen.blit(self.explosion2, [self.x - change_coo, self.y - change_coo])
        elif current_tick - self.shot_end_tick < 270:
            self.screen.blit(self.explosion3, [self.x - change_coo, self.y - change_coo])
        elif current_tick - self.shot_end_tick < 320:
            self.screen.blit(self.explosion4, [self.x - change_coo, self.y - change_coo])


    def draw_bullet(self):
        copied_bullet = self.copy_rotate(self.image, self.angle - 90)
        
        change_coo_x = copied_bullet.get_rect().center[0]
        change_coo_y = copied_bullet.get_rect().center[1]

        self.screen.blit(copied_bullet, [self.x - change_coo_x , self.y - change_coo_y ])


    def beyond_screen(self):
        #hardcoding width and height of the screen
        if self.y < 0 or self.y > 850 or self.x < 0 or self.x > 1200:
            return True
        return False

    


        ##### don't shoot if 
        