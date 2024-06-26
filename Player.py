class Player:
    import pygame
    import os
    path = "Assets/Characters"
    sprites_dimensions = (40, 14)  # Las dimenciones respecto a la pantalla

    def __init__(self):
        self.character = 'Mario'  # Indica el personaje que por defecto es Mario
        self.sprites = self.load_everything()  # Carga y ajusta la resolucion de las sprites
        self.sprites_for_selection_screen = self.load_for_select()  # Carga y ajusta la resolucion de las sprites
        self.casillas = self.get_board_positions(mapped=True)  # Son las posiciones de las casillas
        self.casilla = 0
        self.row = 0
        self.position = self.casillas[self.casilla]  # Es la posicion del personaje en pantalla
        self.current_animation = 'IDLE'  # Indica la animacion actual
        self.current_frame = 0  # Mantiene el registro del numero de frame
        self.facing = True  # Si es verdad el personaje ve a la derecha si es falso a la izquierda
        self.dead = False
        self.regulation = 8  # Regula el tiempo en base a self.fps
        self.fps = 0  # Incrementa su valor hasta sesenta hasa llegar a 24 luego vuelve a cero

    def load_everything(self) \
            -> dict:
        """
        :return: un diccionario que contiene los datos de los sprites de las diferentes animaciones del personaje
        """

        idle_animation = [self.pygame.image.load(f"{Player.path}/{self.character}/IDLE/{sprite}")
                          for sprite in self.os.listdir(f"{Player.path}/{self.character}/IDLE")]

        spring_animation = [self.pygame.image.load(f"{Player.path}/{self.character}/Spring/{sprite}")
                            for sprite in self.os.listdir(f"{Player.path}/{self.character}/Spring")]

        idle_animation = self.scaling(idle_animation)
        spring_animation = self.scaling(spring_animation)
        sprites = {
                   'IDLE': idle_animation,
                   'Spring': spring_animation}
        return sprites

    def load_for_select(self) \
            -> dict:

        select = [self.pygame.image.load(f"{Player.path}/{self.character}/Select_screen/{sprite}")
                  for sprite in self.os.listdir(f"{Player.path}/{self.character}/Select_screen")]

        select = self.scaling_selection_character(select)
        lista_de_sprites = {'self': self,
                            'select': select}
        return lista_de_sprites

    def getting_rect(self) \
            -> pygame.Rect:
        """
        :return: Rectangulo para calcular posicion y colisiones de los personajes
        """
        resolution = self.get_resolution()
        size_to_scale = (resolution[0] / Player.sprites_dimensions[0],
                         resolution[1] / Player.sprites_dimensions[1])
        rect = self.pygame.Rect(self.position, size_to_scale)
        return rect

    def scaling(self, sprites: list) \
            -> list:
        """
        :param sprites: lista de sprites para ajustar tamano
        :return: lista con las sprites ya asjustadas
        """

        resolution = self.get_resolution()
        size_to_scale = (resolution[0] / Player.sprites_dimensions[0],
                         resolution[1] / Player.sprites_dimensions[1])
        scaled_sprites = []
        for sprite in sprites:
            scaled_sprites.append(self.pygame.transform.scale(sprite, size_to_scale))
        return scaled_sprites

    def give_frame(self) \
            -> list:
        """
        :return: La frame actual de la animacion actual
        """
        if self.row % 2 == 1:
            self.facing = False
        else:
            self.facing = True
        if self.character == 'Sonic':
            self.regulation = 2
        if len(self.sprites[self.current_animation]) <= self.current_frame:
            self.current_frame = 0

        if self.fps % self.regulation == 0:
            returning_frame = self.sprites[self.current_animation][self.current_frame]
            self.current_frame += 1
        else:
            returning_frame = self.sprites[self.current_animation][self.current_frame]

        if not self.facing:
            returning_frame = self.pygame.transform.flip(returning_frame, True, False)

        # Aumenta y regula el valor de self.fps
        self.fps += 1
        if self.fps == 24:
            self.fps = 0

        return [returning_frame, self.position]

    def selection_character_give_frame(self) \
            -> object:
        """
        :return: La frame actual de la animacion de idle
        """
        if self.character == 'Sonic':
            self.regulation = 2
        # Si el indice de la animacion es mayor a la cantidad de datos de la animacion
        # vuelve a empezar desde zero
        if len(self.sprites_for_selection_screen['select']) <= self.current_frame:
            self.current_frame = 0

        # Regula la velocidad a la que se muestra la animacion
        if self.fps % self.regulation == 0:
            returning_frame = self.sprites_for_selection_screen["select"][self.current_frame]
            self.current_frame += 1
        else:
            returning_frame = self.sprites_for_selection_screen["select"][self.current_frame]

        # Aumenta y regula el valor de self.fps
        self.fps += 1
        if self.fps == 24:
            self.fps = 0
        return returning_frame

    def scaling_selection_character(self, frames) -> list:

        resolution = self.get_resolution()
        scaled_frames = []
        size_to_scale = (resolution[0] / (Player.sprites_dimensions[0] / 5.5),
                         resolution[1] / (Player.sprites_dimensions[1] / 5.5)
                         )
        for frame in frames:
            scaled_frames.append(self.pygame.transform.scale(frame, size_to_scale))
        return scaled_frames

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

    def move_x(self, target_casilla):
        if self.row % 2 == 0:
            self.position[0] += 5
            if self.position[0] >= self.casillas[target_casilla][0]:
                self.position[0] = self.casillas[target_casilla][0]
                return True
            else:
                return False
        else:
            self.position[0] -= 5
            if self.position[0] <= self.casillas[target_casilla][0]:
                self.position[0] = self.casillas[target_casilla][0]
                return True
            else:
                return False

    def move_y(self, casilla):
        if self.casillas[self.casilla][1] != self.casillas[casilla][1]:
            self.position[1] -= 5
            if self.position[1] <= self.casillas[casilla][1]:
                self.position[1] = self.casillas[casilla][1]
                return True
            else:
                return False

    def moving(self, casillas_a_mover: list):
        row_num = 12
        rows = []
        for i in range(8):
            rows.append([x for x in range(row_num-12, row_num)])
            row_num += 12
        done = False
        target_casilla = self.casilla + casillas_a_mover[0]

        if self.row + 1 < 8 and not done:
            if target_casilla in rows[self.row]:
                self.move_x(target_casilla)


            elif target_casilla in rows[self.row + 1]:
                if self.position[0] != self.casillas[rows[self.row][11]][0]:
                    self.move_x(rows[self.row][11])
                else:
                    up = self.move_y(target_casilla)
                    if up:
                        self.row += 1

        else:
            if target_casilla in rows[self.row]:
                self.move_x(target_casilla)
            else:
                target_casilla = rows[self.row][11]
                self.move_x(target_casilla)
        if self.position == self.casillas[target_casilla]:
            done = True
            self.casilla = target_casilla
        return done

    def death(self):
        pass