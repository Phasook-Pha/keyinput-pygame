import pygame

def set_caption(icon_path, caption):
    # Setting the Window's title
    pygame.display.set_caption(caption)

    # Setting the window's icon
    icon = pygame.image.load(icon_path)
    pygame.display.set_icon(icon)