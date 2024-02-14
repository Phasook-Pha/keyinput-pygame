import pygame

def move_obj(ori_position, current_position, change_position, limits, cond_status):
    new_position = current_position.copy()
    for index, changes in enumerate(change_position):
        new_position[index] += changes
        if new_position[index] <= 0 or new_position[index] >= limits[index]:
            # Exceed the screen
            status = False
            new_position = list(ori_position)
            break
        else:
            # Still witnin the screen
            status = True
            if cond_status == True:
                new_position[index] = new_position[index]
            else:
                new_position = list(ori_position)
    return new_position, status

def key_read(key_read):
    init_x = 0
    init_y = 0
    if key_read[pygame.K_RIGHT] == True:
        move_x = 1
        if key_read[pygame.K_UP] == True:
            move_y = -1
        elif key_read[pygame.K_DOWN] == True:
            move_y = 1
        else:
            move_y = init_y
    elif key_read[pygame.K_LEFT] == True:
        move_x = -1
        if key_read[pygame.K_UP] == True:
            move_y = -1
        elif key_read[pygame.K_DOWN] == True:
            move_y = 1
        else:
            move_y = init_y
    else:
        move_x = init_x
        if key_read[pygame.K_UP] == True:
            move_y = -1
        elif key_read[pygame.K_DOWN] == True:
            move_y = 1
        else:
            move_y = init_y
    return [move_x, move_y]

def mouse_read(init_position):
    def get_click():
        mouse_click = pygame.mouse.get_pressed()
        return mouse_click
    def get_move():
        mouse_move = pygame.MOUSEMOTION
        mouse_pos = pygame.mouse.get_pos()
        return mouse_move, mouse_pos

    left_click, middle_click, right_click = get_click()
    if left_click == True:
        move_status, mouse_position = get_move()
        if move_status == False:
            # Grab Object (No Moving)
            mouse_position = [0, 0]
        else:
            # Grab & Move Object
            mouse_position = list(mouse_position)
            for i, pos in enumerate(init_position):
                mouse_position[i] -= pos
    else:
        # Do Nothing
        mouse_position = [0, 0]
    return mouse_position