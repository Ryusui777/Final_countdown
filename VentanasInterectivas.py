import pygame
import sys
from Botones import Button

pygame.init()

WIDHT, HEIGHT= 1280,720
window= pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Mario 3")
fondo=pygame.transform.scale(pygame.image.load( "FondoPerosnajes.jpg"), (WIDHT, HEIGHT))

def letra(size):
    return pygame.font.Font("assents/font.ttf", size)

def menu_principal():
    pygame.display.set_caption("Menu principal")

    while True:
        window.blit(fondo,(0,0))

        posicion_del_mouse_menu= pygame.mouse.get_pos()

        menu_texto= letra(100).render("Menu Principal", True, "#b68f40")
        menu_rect= menu_texto.get_rect(centro= (640, 100))

        boton_jugar= Button (image=pygame.image.load("assets/Play FondoPersonajes.png"), posicion=(640, 250), 
                            texto_entrada= "Jugar", fuente= letra(75), color_base= "Black", hovering_color="Green")
        boton_reglas= Button (image=pygame.image.load("assets/Reglas FondoPersonajes.png"), posicion=(640, 400), 
                            texto_entrada= "Reglas", fuente= letra(75), color_base= "Black", hovering_color="Green")
        boton_salir= Button (image=pygame.image.load("assets/Salir FondoPersonajes.png"), posicion=(640, 550), 
                            texto_entrada= "Salir", fuente= letra(75), color_base= "Black", hovering_color="Green")
    
        window.blit( menu_texto, menu_rect )

        for button in [boton_jugar, boton_reglas, boton_salir]:
            button.cambiar_color(posicion_del_mouse_menu)
            button.actualizar(window)

        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.checkForInput(posicion_del_mouse_menu):
                    Jugar()
                if boton_reglas.checkForInput(posicion_del_mouse_menu):
                    Reglas()
                if boton_salir.checkForInput(posicion_del_mouse_menu):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu_principal()