#tank_shells
import pygame
import math
from pygame.sprite import Sprite
class Shell(Sprite):
    def __init__(self, image, screen, player, mouse_pos):
        super(Shell, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (15,15))
        self.screen = screen
        self.speed = 10
        self.x = player.x_top #+ self.speed # why
        self.y = player.y_top
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.angle = player.top_angle

        self.start_x = player.x_top

        self.mouse_pos = mouse_pos

    def update(self, player):
        #make it explode at the mouse positin
        angle_radians = self.angle * math.pi / 180
        x2 = self.mouse_pos[0]
        y2 = self.mouse_pos[1]
        start_x = self.start_x
        shot_length = (x2 - start_x) / math.cos(angle_radians)
        shot_length_real = (self.x - start_x )/ math.cos(angle_radians)
        #or make it simpler like that? x2 = self.x
        if shot_length > shot_length_real:
            self.x += self.speed * math.cos(angle_radians)
            self.y -= self.speed * math.sin(angle_radians)
            print shot_length, shot_length_real 
            # print self.x, start_x
        else:
            print "stopped shooting"
            return
        
        ######Rotate the image while shoot
        ######Change the center of the self.x and y
        ####### 
            
            


        # while shot_length > shot_lenth_real:
        #     self.x += self.speed * math.cos(angle_radians)
        #     self.y -= self.speed * math.sin(angle_radians)
        #     shot_length_real = math.fabs((self.x - start_x )/ math.cos(angle_radians))

        #add explosion here
            



    def draw_shell(self):
        self.screen.blit(self.image, [self.x, self.y])

    def beyond_screen(self):
        #hardcoding width and height of the screen
        if self.y < 0 or self.y > 850 or self.x < 0 or self.x > 1200:
            return True
        return False
        