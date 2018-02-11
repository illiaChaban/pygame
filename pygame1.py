import pygame
from player_tank import Player
import math 
# from pygame.sprite import Group, groupcollide

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275



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
    
    #
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
            elif event.type == pygame.KEYDOWN:
                if event.key == KEY_UP:

                    the_player.move_up()
                    
                if event.key == KEY_DOWN:
                    the_player.move_down()

                if event.key == KEY_LEFT:
                    the_player.turn_left()
                if event.key == KEY_RIGHT:
                    the_player.turn_right()

            elif event.type == pygame.KEYUP:
                if event.key == KEY_UP:
                    the_player.stop()
                if event.key == KEY_DOWN:
                    the_player.stop()
                if event.key == KEY_RIGHT:
                    the_player.stop_turn()
                if event.key == KEY_LEFT:
                    the_player.stop_turn()        

            elif event.type == pygame.MOUSEMOTION:
                pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass         
            # if event.type == pygame.KEYUP:
                        
            #     the_player.bottom_angle += 3
           
        # Game logic
        the_player.update()
        

        # Draw background
   
        screen.blit(background, [0,0])
        pygame.draw.circle(screen, (255, 0, 0), (500, 250), 50, 0)
        the_player.draw_me()
        

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
