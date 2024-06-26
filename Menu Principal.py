import pygame
import sys
from Botones import Button
from screeninfo import get_monitors
from char_select_win import SelectWindow  
import Player

def get_resolution() -> tuple:
    screen = [monitor for monitor in get_monitors()]
    for primary_screen in screen:
        if primary_screen.is_primary:
            size_tup = (primary_screen.width - (primary_screen.width / 384),
                        primary_screen.height - (primary_screen.height / 13.5))
            return size_tup

resolution = get_resolution()
print(resolution)

pygame.init()
window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Mario 3")
fondo = pygame.transform.scale(pygame.image.load("Pantalla Super Mario.jpeg"), resolution)

def letra(size):
    return pygame.font.Font("font.ttf", size)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption("Mario Bros")
        self.clock = pygame.time.Clock()
        self.state = "Menu_principal"
        self.states = {
            "Menu_principal": self.menu_principal,
            "Reglas": self.reglas,
            "Char_Select": self.char_select_win  # Nuevo estado
        }

    def set_state(self, new_state):
        self.state = new_state

    def menu_principal(self):
        BG = pygame.transform.scale(pygame.image.load("Assets/bg/Select_screen.png"), resolution)
        boton_jugar = Button(imagen=pygame.image.load("Rect.png"), posicion=(resolution[0] / 2, resolution[1] / 2 - 175), texto_entrada="Jugar", fuente=letra(75), color_base="White", hovering_color="Green")
        boton_reglas = Button(imagen=pygame.image.load("Rect.png"), posicion=(resolution[0] / 2, resolution[1] / 2), texto_entrada="Reglas", fuente=letra(75), color_base="White", hovering_color="Purple")
        boton_salir = Button(imagen=pygame.image.load("Rect.png"), posicion=(resolution[0] / 2, resolution[1] / 2 + 175), texto_entrada="Salir", fuente=letra(75), color_base="White", hovering_color="Red")

        while self.state == "Menu_principal":
            self.screen.blit(BG, (0, 0))
            menu_texto = letra(70).render("Super Mario Bros", True, "White")
            menu_rect = menu_texto.get_rect(center=(resolution[0] / 2, resolution[1] / 2 - 400))
            self.screen.blit(menu_texto, menu_rect)
            
            mouse_pos = pygame.mouse.get_pos()
            
            for button in [boton_jugar, boton_reglas, boton_salir]:
                button.cambiar_color(mouse_pos)
                button.actualizar(self.screen)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_jugar.verificar_input(mouse_pos):
                        self.set_state("Char_Select")  # Cambiar al nuevo estado
                    if boton_reglas.verificar_input(mouse_pos):
                        self.set_state("Reglas")
                    if boton_salir.verificar_input(mouse_pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

    def char_select_win(self):
        win = SelectWindow()
        players = [Player.Player(), Player.Player(), Player.Player()]
        loaded_players = [player.selection_character_give_frame() for player in players]
        run = True
        clock = pygame.time.Clock()
        win.refresh(loaded_players)
        
        mas_imgen = pygame.image.load("mas.png")
        mas_imgen = pygame.transform.scale(mas_imgen, (100, 100)) 
        boton_mas = Button(imagen=mas_imgen, posicion=(resolution[0] -135, resolution[1] - 400),
                                        texto_entrada=None, fuente=letra(75), color_base="White", hovering_color="white")
        

        menos_imgen = pygame.image.load("menos.png")
        menos_imgen = pygame.transform.scale(menos_imgen, (100, 100)) 
        boton_menos = Button(imagen=menos_imgen, posicion=(resolution[0] -135, resolution[1]  - 270),
                                        texto_entrada=None, fuente=letra(75), color_base="White", hovering_color="white")
        
        derecha_imgen = pygame.image.load("Flecha para la derecha.png")
        derecha_imgen = pygame.transform.scale(derecha_imgen, (80, 80)) 
        boton_derecha = Button(imagen=derecha_imgen, posicion=(resolution[0]/2+170, resolution[1]/2 -350),
                                        texto_entrada=None, fuente=letra(75), color_base="White", hovering_color="white")
        

        izquierda_imgen = pygame.image.load("Flecha para la izquierda.png")
        izquierda_imgen = pygame.transform.scale(izquierda_imgen, (80, 80)) 
        boton_izquierda = Button(imagen=izquierda_imgen, posicion=(resolution[0] / 2 + -170, resolution[1] / 2 - 350),
                                        texto_entrada=None, fuente=letra(75), color_base="White", hovering_color="white")
        
        boton_volver = Button(imagen=None, posicion=(resolution[0] / 2 - 720, resolution[1] / 2 + 400),
                               texto_entrada="Volver", fuente=letra(50), color_base="white", hovering_color="Yellow")
        
        boton_iniciar = Button(imagen=None, posicion=(resolution[0] / 2 + 720, resolution[1] / 2 +400 ),
                               texto_entrada="Iniciar", fuente=letra(50), color_base="white", hovering_color="Green")
        
        while self.state == "Char_Select":
            clock.tick(24)
            loaded_players = [player.selection_character_give_frame() for player in players]
            win.refresh(loaded_players)
            
            mouse_pos = pygame.mouse.get_pos()
            
            for button in [boton_mas,boton_menos,boton_derecha,boton_izquierda, boton_volver,boton_iniciar]:
                button.cambiar_color(mouse_pos)
                button.actualizar(win.window_object)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_volver.verificar_input(mouse_pos):
                        self.set_state("Menu_principal")
            
            pygame.display.update()

    def reglas(self):
        pygame.display.set_caption("Reglas")
        reglas_volver = Button(imagen=None, posicion=(resolution[0] / 2 - 720, resolution[1] / 2 + 400),
                               texto_entrada="Volver", fuente=letra(50), color_base="Black", hovering_color="Yellow")

        while self.state == "Reglas":
            mouse_pos = pygame.mouse.get_pos()
            self.screen.fill("white")

            reglas_texto = letra(30).render("Esta ventana son las reglas del juego", True, "Black")
            reglas_rect = reglas_texto.get_rect(center=(resolution[0] / 2, resolution[1] / 2 - 175))
            self.screen.blit(reglas_texto, reglas_rect)

            reglas_volver.cambiar_color(mouse_pos)
            reglas_volver.actualizar(self.screen)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if reglas_volver.verificar_input(mouse_pos):
                        self.set_state("Menu_principal")
            pygame.display.update()

    def run(self):
        while True:
            self.states[self.state]()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
