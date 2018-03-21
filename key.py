import pygame

def any_of_keys_pressed(key_list):
    try:
        for key in key_list:
            if pygame.key.get_pressed()[key] == 1:
                return True
    except ValueError:
        return False

def move_forward_pressed():    
    return any_of_keys_pressed([119, 273])

def move_back_pressed():
    return any_of_keys_pressed([115, 274])

def turn_left_pressed():
    return any_of_keys_pressed([97, 276])

def turn_right_pressed():
    return any_of_keys_pressed([100, 275])

