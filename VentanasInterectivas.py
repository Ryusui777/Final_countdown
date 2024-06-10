import pygame
import sys
from Botones import Button
from screeninfo import get_monitors

resolution = get_monitors()
print(resolution)
resolution = (resolution[1].width-(resolution[1].width/384),resolution[1].height-(resolution[1].height/13.5))

pygame.init()

window= pygame.display.set_mode(resolution)
pygame.display.set_caption("Mario 3")
fondo=pygame.transform.scale(pygame.image.load( "Pantalla Super Mario.jpeg"), (resolution))

def letra(size):
    return pygame.font.Font("font.ttf", size)

def Jugar():
    pygame.display.set_caption("Jugar")

    while True:
        posicion_del_mouse_jugar= pygame.mouse.get_pos()
        window.fill("Black")

        jugar_texto= letra(30).render("Esta ventana redirige al juego", True, "White")
        jugar_rect= jugar_texto.get_rect(center= (640, 260))
        window.blit( jugar_texto, jugar_rect )

        jugar_volver= Button(imagen=None, posicion=(640,460), texto_entrada= "Volver", fuente= letra(75), color_base= "White", hovering_color="Green")

        jugar_volver.cambiar_color(posicion_del_mouse_jugar)
        jugar_volver.actualizar(window)

        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if jugar_volver.verificar_input(posicion_del_mouse_jugar):
                    menu_principal()
                    
        pygame.display.update()

    
def Reglas():
    pygame.display.set_caption("Reglas")

    while True:
        posicion_del_mouse_reglas= pygame.mouse.get_pos()
        window.fill("white")

        reglas_texto= letra(30).render("Esta ventana son las reglas del juego", True, "Black")
        reglas_rect= reglas_texto.get_rect(center= (640, 260))
        window.blit( reglas_texto, reglas_rect)

        reglas_volver= Button(imagen=None, posicion=(640,460), texto_entrada= "Volver", fuente= letra(75), color_base= "Black", hovering_color="Green")

        reglas_volver.cambiar_color(posicion_del_mouse_reglas)
        reglas_volver.actualizar(window)

        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if reglas_volver.verificar_input(posicion_del_mouse_reglas):
                    menu_principal()
                    
        pygame.display.update()

def menu_principal():
    pygame.display.set_caption("Menu principal")

    while True:
        window.blit(fondo,(0,0))

        posicion_del_mouse_menu= pygame.mouse.get_pos()
        
        SuperMario_imagen = pygame.image.load("Rect.png")
        SuperMario_rect = SuperMario_imagen.get_rect(center=(350, 100 ))

        SuperMario_imagen2 = pygame.image.load("Rect.png")
        SuperMario_rect2 = SuperMario_imagen2.get_rect(center=(935, 100 ))

        menu_texto= letra(70).render("Super Mario Bros", True, "White")
        menu_rect= menu_texto.get_rect(center= (640, 100))

        boton_jugar= Button (imagen=pygame.image.load("Rect.png"), posicion=(640, 250), 
                            texto_entrada= "Jugar", fuente= letra(75), color_base= "White", hovering_color="Green")
        boton_reglas= Button (imagen=pygame.image.load("Rect.png"), posicion=(640, 400), 
                            texto_entrada= "Reglas", fuente= letra(75), color_base= "White", hovering_color="Purple")
        boton_salir= Button (imagen=pygame.image.load("Rect.png"), posicion=(640, 550), 
                            texto_entrada= "Salir", fuente= letra(75), color_base= "White", hovering_color="Red")
    
        window.blit( SuperMario_imagen,SuperMario_rect,)
        window.blit(SuperMario_imagen2,SuperMario_rect2)
        window.blit( menu_texto, menu_rect )

        for button in [boton_jugar, boton_reglas, boton_salir]:
            button.cambiar_color(posicion_del_mouse_menu)
            button.actualizar(window)

        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.verificar_input(posicion_del_mouse_menu):
                    Jugar()
                if boton_reglas.verificar_input(posicion_del_mouse_menu):
                    Reglas()
                if boton_salir.verificar_input(posicion_del_mouse_menu):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu_principal()