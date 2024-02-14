import pygame

def create_obj(screen, img_path, coor, size):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, size)
    screen.blit(img, coor)

def create_txt(screen, text, font_style, font_size, bold, color, coor):
    text_style = pygame.font.SysFont(font_style, font_size, bold = bold)
    text_img = text_style.render(text, False, color)
    screen.blit(text_img, coor)