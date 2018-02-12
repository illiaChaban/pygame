import pygame
from player_tank import Player
import math 
import time
# from pygame.sprite import Group, groupcollide

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

black = (0, 0, 0)

# def gameStart():
# 	myFont = pygame.font.SysFont("monaco", 72)
# 	GOsurf = myFont.render("Fight! ", True, black) ##true is to make it antialiased 
# 	GOrect = GOsurf.get_rect()
# 	GOrect.midtop = (360, 15)
# 	screen.blit(GOsurf, GOrect)
# 	pygame.display.flip()
# 	time.sleep(4)
# 	pygame.quit()

def main():
    width = 1200
    height = 850
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tanks')
    clock = pygame.time.Clock()
    background = pygame.image.load('images/background_desert1.png')
    background = pygame.transform.scale(background, (width,height))
    the_player = Player("images/tank_bottom_new_cropped1.png", "images/tank_top_new_cropped.png", 350, 350, screen)
    
    #
    #what does this do???? 
    # player_group = Group()
    # player_group.add(the_player)

    # Game initialization

    # gameStart()
    
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
            elif event.type == pygame.KEYDOWN:
                #move back and forth
                if event.key == KEY_UP or event.key == ord('w'):
                    the_player.move_up()
                if event.key == KEY_DOWN or event.key == ord('s'):
                    the_player.move_down()

                #change bottom_angle
                if event.key == KEY_LEFT or event.key == ord('a'):
                    the_player.turn_left()
                if event.key == KEY_RIGHT or event.key == ord('d'):
                    the_player.turn_right()

            elif event.type == pygame.KEYUP:
                if event.key == KEY_UP or event.key == ord('w'):
                    the_player.stop()
                if event.key == KEY_DOWN or event.key == ord('s'):
                    the_player.stop()
                if event.key == KEY_RIGHT or event.key == ord('d'):
                    the_player.stop_turn()
                if event.key == KEY_LEFT or event.key == ord('a'):
                    the_player.stop_turn()        

            elif event.type == pygame.MOUSEMOTION:
                pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                the_player.shoot()
                # if event.key          
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
