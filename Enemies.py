
class Enemies:
    import pygame
    import os
    path = 'Assets\Enemies'
    sprites_dimensions = (40, 14)

    def __init__(self):
        # making blooper enemie
        self.enemie = 'blooper'
        self.current_frame = 0
        self.sprites = self.load_sprites()
        self.make_enemie()


    def make_enemie(self):
        match self.enemie:
            case 'blooper':
                pass


    def give_frame(self):
        lista_de_enemigos = []

    def change_frame(self):
        pass

    def load_sprites(self):
        pass


    @staticmethod
    def get_resolution() \
            -> tuple:
        """
        :return: tuple con las medidas adecuadas para la resolucion de la ventana relativo al tamano del monitor
        """
        from screeninfo import get_monitors
        screen = [monitor for monitor in get_monitors()]
        for primary_screen in screen:
            if primary_screen.is_primary:
                size_tup = (primary_screen.width - (primary_screen.width / 384),
                            primary_screen.height - (primary_screen.height / 13.5))
                return size_tup

    def get_board_positions(self, mapped: bool) \
            -> list:
        """
        :return: Lista con las posiciones de las casillas, segun valores predefinidos
        """
        resolution = self.get_resolution()
        x_vals = [4, 3.25, 2.67, 2.277, 1.97, 1.74, 1.56, 1.415, 1.292, 1.19, 1.106, 1.03]
        y_vals = [1.14, 1.325, 1.6, 2, 2.7, 4.1, 8.7, 100]
        casillas = [[resolution[0] / x for x in x_vals],
                    [resolution[1] / y for y in y_vals]]
        mapped_casillas = []
        for casilla_y in range(8):

            if casilla_y % 2 == 0:
                for casilla_x in casillas[0]:
                    mapped_casillas.append([casilla_x, casillas[1][casilla_y]])
            else:
                for casilla_x in reversed(casillas[0]):
                    mapped_casillas.append([casilla_x, casillas[1][casilla_y]])
        if mapped:
            return mapped_casillas
        else:
            return casillas






