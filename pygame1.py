import pygame
from player_tank import Player
import math 
import time
from pygame.sprite import Group, groupcollide # why do we need it????
from Shell import Shell
from collision import Block

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
    # width = 1200
    # height = 850
    width = 700
    height = 600
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tanks')
    clock = pygame.time.Clock()
    background = pygame.image.load('images/background_desert1.png')
    background = pygame.transform.scale(background, (width,height))
    the_player = Player("images/tank_bottom_new_cropped3.png", "images/tank_top_new_cropped7.png", 350, 350, screen)
    #do we even need this?
    players = Group()
    players.add(the_player)
    #
    square = Block( 200, 200, (0,0,0) , 50, 50, screen)
    players.add(square)
    
    shells = Group()
    

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
                # print math.fabs((pygame.mouse.get_pos()[0] - the_player.x) / math.cos(the_player.top_angle_rad))
                x2 = pygame.mouse.get_pos()[0]
                y2 = pygame.mouse.get_pos()[1]
                
                current_tick = pygame.time.get_ticks()
                

                if (current_tick - the_player.last_shot_tick) > the_player.cool_down:

                
                    shot_length = math.sqrt((x2 - the_player.x)**2 +(y2 - the_player.y)**2)
                    # print shot_length
                    if shot_length > 85:
                        new_shell = Shell("images/tank_shell5.png", screen, the_player)   #tank_shell1_cropped.png
                        shells.add(new_shell)
                        the_player.last_shot_tick = new_shell.shot_start_tick
                        

                # elif current_tick - the_player.last_shot_tick < 175:
                #     screen.blit()
                # the_player.shoot()
                # if event.key          
            # if event.type == pygame.KEYUP:
                        
            #     the_player.bottom_angle += 3
           
        # Game logic
        the_player.update(players)
        

        # Draw background
   
        screen.blit(background, [0,0])
        
        
        

       
        

        # Game display
        square.render(the_player)
        the_player.draw_me()

        #shell display
        for shell in shells:
            shell.update(the_player)
            shell.draw_shot()
            if shell.beyond_screen():
                shells.remove(shell)
                #or if shell reached mouse_pos
                
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
