#tank_shells
import pygame
import math
from pygame.sprite import Sprite
class Shell(Sprite):
    def __init__(self, image, screen, player, mouse_pos):
        super(Shell, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (5,15))
        self.screen = screen
        self.speed = 40
        self.x = player.x_top #+ self.speed # why
        self.y = player.y_top
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.angle = player.top_angle

        self.start_x = player.x_top
        self.start_y = player.y_top

        self.mouse_pos = mouse_pos

    def update(self, player):
        #make it explode at the mouse positin
        angle_radians = self.angle * math.pi / 180
        x2 = self.mouse_pos[0]
        y2 = self.mouse_pos[1]
        
        # shot_length = (x2 - self.start_x) / math.cos(angle_radians)
        # shot_length_real = (self.x - self.start_x )/ math.cos(angle_radians)

        shot_length = math.sqrt((x2 - self.start_x)**2 +(y2 - self.start_y)**2)
        shot_length_real = math.sqrt((self.x - self.start_x)**2 + (self.y - self.start_y)**2)

        #or make it simpler like that? x2 = self.x
        if (shot_length - shot_length_real) < self.speed:
            self.x = x2
            self.y = y2
        elif shot_length > shot_length_real:
            
            self.x += self.speed * math.cos(angle_radians)
            self.y -= self.speed * math.sin(angle_radians)
            print shot_length, shot_length_real 
            # print self.x, start_x

            ## change self.x, y like top_image
        else:
            self.x = x2
            self.y = y2
            print "stopped shooting"
            ##add explosion
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
        copied_image = self.image.copy()
        copied_image = pygame.transform.rotate(copied_image, self.angle - 90)
        width = copied_image.get_rect()[2]
        height = copied_image.get_rect()[3]
        change_coo_x = (width - self.rect[2]) / 2
        change_coo_y = (height - self.rect[3]) / 2
        self.screen.blit(copied_image, [self.x - change_coo_x, self.y - change_coo_y])

        # self.screen.blit(self.image, [self.x, self.y])

    def beyond_screen(self):
        #hardcoding width and height of the screen
        if self.y < 0 or self.y > 850 or self.x < 0 or self.x > 1200:
            return True
        return False
        