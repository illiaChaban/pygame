#tank_shells
import pygame
import math
from pygame.sprite import Sprite
class Shell(Sprite):
    def __init__(self, image, screen, player): #, mouse_pos):
        super(Shell, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (20,15))
        self.screen = screen
        self.speed = 20
        
        self.angle = player.top_angle
        self.angle_rad = self.angle * math.pi / 180

        self.shot_length = 0
        self.shot_length_current = 0

        self.start_x = player.x + math.cos(self.angle_rad)* 50 #_top
        self.start_y = player.y - math.sin(self.angle_rad)* 50 #_top

        # self.mouse_pos = mouse_pos

        self.x = self.start_x  #+ self.speed # why
        self.y = self.start_y 
        
        self.mouse_pos = pygame.mouse.get_pos() #self.mouse_pos[0]

         #add fire the moment tank shoots
        self.fire0 = pygame.image.load("images/tank_fire0.png")
        self.fire0 = pygame.transform.scale(self.fire0, (40,40))
        
        self.fire1 = pygame.image.load("images/tank_fire1.png")
        self.fire1 = pygame.transform.scale(self.fire1, (40,40))

        self.fire2 = pygame.image.load("images/tank_fire2.png")
        self.fire2 = pygame.transform.scale(self.fire2, (40,40))
        

    def update(self, player):

        
        #make it explode at the mouse positin
        angle_radians = self.angle * math.pi / 180
        x2 = self.mouse_pos[0]
        y2 = self.mouse_pos[1]
        
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

        shot_length = math.sqrt((x2 - self.start_x)**2 +(y2 - self.start_y)**2)
        shot_length_real = math.sqrt((self.x - self.start_x)**2 + (self.y - self.start_y)**2)
        
        self.shot_length = shot_length
        self.shot_length_current = shot_length_real
        
        if (shot_length - shot_length_real) < self.speed:
            self.x = x2
            self.y = y2
            #i can put it beyond the screen instead
        elif shot_length > shot_length_real:
            
            self.x += self.speed * math.cos(angle_radians)
            self.y -= self.speed * math.sin(angle_radians)
            # self.y -= math.sqrt((self.speed ** 2) - (self.speed * math.cos(angle_radians))**2)
            
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

        
        # self.fire0 = pygame.transform.rotate(self.fire0, self.angle - 90)
        # self.fire1 = pygame.transform.rotate(self.fire1, self.angle - 90)
        # self.fire2 = pygame.transform.rotate(self.fire2, self.angle - 90)

        change_x0 = self.fire0.get_rect().center[0]
        change_y0 = self.fire0.get_rect().center[1]

        change_x1 = self.fire1.get_rect().center[0]
        change_y1 = self.fire1.get_rect().center[1]

        change_x2 = self.fire2.get_rect().center[0]
        change_y2 = self.fire2.get_rect().center[1]
       
        if (self.shot_length > 80):
            # print self.shot_length
            # print self.shot_length_current
            if self.shot_length_current < 23:
                self.screen.blit(self.fire0, [self.start_x - change_x0, self.start_y - change_y0])
                
            elif self.shot_length_current < 63:
                self.screen.blit(self.fire1, [self.start_x - change_x0, self.start_y - change_y0])
            elif self.shot_length_current < 80:
                self.screen.blit( self.fire2, [self.start_x - change_x0, self.start_y - change_y0])
            else:
                pass
        elif self.shot_length > 25:
            if self.shot_length_current < 20:
                self.screen.blit(self.fire1, [self.start_x - change_x0, self.start_y - change_y0])
            elif self.shot_length_current < 25:
                self.screen.blit(self.fire2, [self.start_x - change_x0, self.start_y - change_y0])
            else: 
                pass
            pass


        copied_image = self.image.copy()
        copied_image = pygame.transform.rotate(copied_image, self.angle - 90)
       
        change_coo_x = self.image.get_rect().center[0]
        change_coo_y = self.image.get_rect().center[1]

        self.screen.blit(copied_image, [self.x - change_coo_x , self.y - change_coo_y ])

        # self.screen.blit(copied_image, [self.x, self.y])

    def beyond_screen(self):
        #hardcoding width and height of the screen
        if self.y < 0 or self.y > 850 or self.x < 0 or self.x > 1200:
            return True
        return False



        ##### don't shoot if 
        