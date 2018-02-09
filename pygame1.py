import pygame
from player_tank import Player
import math 
# from pygame.sprite import Group, groupcollide

def rot_center(image, angle):
    # """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    copy_img = image.copy()
    rot_image = pygame.transform.rotate(copy_img, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image




def main():
    width = 900
    height = 700
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tanks')
    clock = pygame.time.Clock()
    background = pygame.image.load('images/grass.jpg')
    background = pygame.transform.scale(background, (width,height))
    the_player = Player("images/tank-bottom-white.png", "images/tank-top-white.png", 350, 350, screen)

    #what does this do???? 
    # player_group = Group()
    # player_group.add(the_player)

    # Game initialization

    
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True    
            the_player.image_bottom = rot_center(the_player.image_bottom, 3)
           
        # Game logic
        

        # Draw background
        screen.fill(blue_color)
        screen.blit(background, [0,0])
        pygame.draw.circle(screen, (255, 0, 0), (0, 0), 50, 0)
        the_player.draw_me()
        

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
