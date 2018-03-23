import pygame
from player_tank import Player
import math 
import time
from pygame.sprite import Group, groupcollide # why do we need it????
from Shell import Shell
from collision import Block
import key

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

black = (0, 0, 0)

def find_shot_length(player):
    x2 = pygame.mouse.get_pos()[0]
    y2 = pygame.mouse.get_pos()[1]
    return math.sqrt((x2 - player.x)**2 +(y2 - player.y)**2)



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
            key.move_forward_pressed()
            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True

            if key.move_forward_pressed():
                the_player.move_up()
            if key.move_back_pressed():
                the_player.move_down()
            if not key.move_back_pressed() and not key.move_forward_pressed():
                the_player.stop() 

            if key.turn_left_pressed():
                the_player.turn_left()
            if key.turn_right_pressed():
                the_player.turn_right()
            if not key.turn_left_pressed() and not key.turn_right_pressed():
                the_player.stop_turn()    

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                current_tick = pygame.time.get_ticks()
                if (current_tick - the_player.last_shot_tick) > the_player.cool_down:

                    shot_length = find_shot_length(the_player)
                    if shot_length > 85:
                        new_shell = Shell("images/tank_shell5.png", screen, the_player) 
                        shells.add(new_shell)
                        the_player.last_shot_tick = new_shell.shot_start_tick
                        # if new_shell.shot_length == new_shell.shot_length_current:
                        #     print new_shell.shot_length == new_shell.shot_length_current
                        #     print new_shell.shot_length
                        #     del new_shell
                            
                        #     print 'DELETED'
                    
                        

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
            shell.update(the_player, players)
            shell.draw_shot()
            # if shell.beyond_screen():
            #     shells.remove(shell)
                #or if shell reached mouse_pos
                
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
