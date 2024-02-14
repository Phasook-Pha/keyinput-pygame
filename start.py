import pygame
from packages.initialize.display import display_init
from packages.initialize.caption import set_caption
from packages.objects.create import create_obj, create_txt
from packages.movements.moves import move_obj, key_read, mouse_read

# Initialize the screen
width = 1024
height = 720
screen = display_init((width, height))

# Setting the window's icon & title
icon_path = "PyGame_Project/images/logo.png"
title = "Simple Simulation"
set_caption(icon_path, title)

# Object (Structure)
structure_path = "Pygame_Project/images/structure.png"
structure_size = (450, 500)
structure_position = (100, 200)

# Object (Person)
person_path = "Pygame_Project/images/person.png"
person_size = (70, 70)
person_position = (900, 640)

# object (Arrow)
arrow_path = "Pygame_Project/images/arrow.png"
arrow_size = (30, 30)
arrow_position = (person_position[0] + (0.5 * arrow_size[0]), person_position[1] - (1.2 * arrow_size[1]))

# Text Object (Structure Text)
struc_text = "Structure Frame"
struc_font_style = "Arial"
struc_font_size = 30
struc_bold = True
struc_font_color = (0, 0, 0)      # (Red, Green, Blue) value of 0-255
struc_font_position = (structure_position[0], structure_position[1] - 50)

# Text Object (Person Text)
person_text = "person"
person_font_style = "Arial"
person_font_size = 30
person_bold = False
person_font_color = (0, 0, 0)      # (Red, Green, Blue) value of 0-255
person_font_position = (arrow_position[0], arrow_position[1] - 50)

# moving components
structure_moving = list(structure_position)
struc_font_moving = list(struc_font_position)
person_moving = list(person_position)
arrow_moving = list(arrow_position)
ptext_moving = list(person_font_position)
init_status = True

# Render the window
running_state = True
while running_state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Terminate the window when press "close"
            running_state = False
        else:
            # Continue rendering
            pass
    
    # Fill the background color based on (Red, Green, Blue) value of 0-255
    screen.fill((0, 0, 255))
    
    # Draw object
    create_obj(screen, structure_path, structure_moving, structure_size)
    create_obj(screen, person_path, person_moving, person_size)
    create_obj(screen, arrow_path, arrow_moving, arrow_size)
    
    #screen, text, font_style, font_size, bold, color, coor
    create_txt(screen, struc_text, struc_font_style, struc_font_size, 
               struc_bold, struc_font_color, struc_font_moving)
    create_txt(screen, person_text, person_font_style, person_font_size, 
               person_bold, person_font_color, ptext_moving)
    
    key = pygame.key.get_pressed()
    moves = key_read(key)
    move_position = mouse_read(structure_moving)

    person_moving, person_status = move_obj(person_position, person_moving, moves, 
                                            [width, height], init_status)
    arrow_moving, arrow_status = move_obj(arrow_position, arrow_moving, moves, 
                                          [width, height], person_status)
    ptext_moving, ptext_status = move_obj(person_font_position, ptext_moving, moves, 
                                          [width, height], person_status)
    structure_moving, structure_status = move_obj(structure_position, structure_moving, move_position, 
                                          [width, height], init_status)
    struc_font_moving, stext_status = move_obj(struc_font_position, struc_font_moving, move_position, 
                                          [width, height], structure_status)

    #Update the color-filled background
    pygame.display.update()
    #pygame.time.delay(200)