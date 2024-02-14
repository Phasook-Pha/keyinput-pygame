import pygame

def display_init(display_size):
    # Initialize the module
    pygame.init()
    
    # Setting the Window's title
    screen = pygame.display.set_mode((display_size[0], display_size[1]))
    return screen