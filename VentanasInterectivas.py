import pygame
import sys
from Botones import Button

pygame.init()

WIDHT, HEIGHT= 600,600
window= pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Mario 3")
fondo=pygame.transform.scale(pygame.image.load("BG.jpg"), (WIDHT, HEIGHT))

def letra(size):
    return pygame.font.Font("assents/font.ttf", size)

def menu_principal():
    pygame.display.set_caption("Menu principal")

    while True:
        window.blit(fondo,(0,0))

        posicion_del_mouse_menu= pygame.mouse.get_pos()
        menu_texto= letra(100).render("Menu Principal", True, "#b68f40")
        menu_rect= menu_texto.get_rect(centro= (640, 100))
