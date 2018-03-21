#collision
import pygame
from pygame.sprite import Sprite

class Block(Sprite):
    def __init__(self, x, y, color, width, height, screen):
        super(Block,self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.image_red = pygame.Surface([width, height])
        self.image_red.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.screen = screen   
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()

        self.cornersList = self.find_corners()





    def render(self, player):
               
        # def wrapper():
        #     return area(self.cornersList) 
        
        if self.detect_collision(player):
            self.screen.blit(self.image_red, [self.x, self.y])
        else: self.screen.blit(self.image, [self.x, self.y])

        # print '#######', self.x, self.y
        # print '#######', self.x + self.width, self.y + self.height

    def find_corners(self):
        cornersList = []
        top_left_corner = [self.x, self.y]
        top_right_corner = [self.x + self.width, self.y]
        bottom_left_corner = [self.x, self.y + self.height]
        bottom_right_corner = [self.x + self.width, self.y + self.height]

        cornersList.append(top_left_corner)
        cornersList.append(top_right_corner)
        cornersList.append(bottom_left_corner)
        cornersList.append(bottom_right_corner)

        return cornersList

    def it_within_my_area(self, player):
        for corner in player.cornersList:
            if self.point_within_my_area(corner):
                return True
        return False

    def me_within_its_area(self, player):
        for corner in self.cornersList:
            if player.point_within_my_area(corner, player.cornersList):
                return True
        return False



    def detect_collision(self, player):
        return self.it_within_my_area(player) or self.me_within_its_area(player)

    

    def point_within_my_area(self, point_coordinates):
        #x1,y1###############x2,y2#
        #                         #
        #                         #
        #x3,y3###############x4,y4#

        x1 = self.cornersList[0][0]
        y1 = self.cornersList[0][1]
        x4 = self.cornersList[3][0]
        y4 = self.cornersList[3][1]

        p_x = point_coordinates[0]
        p_y = point_coordinates[1]

        return p_x >= x1 and p_x <= x4 and p_y >= y1 and p_y <= y4



    
        

