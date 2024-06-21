
class Dice:
    import pygame

    path = 'C:/Users/david/final_countdown/Game/Assets/dice'

    def __init__(self):
        self.animation = self.load_animations()
        self.location = self.get_location()
        self.current_frame = 0
        self.current_sprite = self.animation[0]
        self.fps = 0
        self.regulation = 6
        self.stop = False

    def give_frame(self) \
            -> list:
        """
        :return: una lista con la sprite correspondiente a la frame para ser proyectada, y su localizacion
        """
        if self.fps % self.regulation == 0:
            if self.current_frame == len(self.animation):
                self.current_frame = 0
            self.current_sprite = self.animation[self.current_frame]
            if not self.stop:
                self.current_frame += 1
            elif self.current_frame % 2 == 1:
                self.current_frame += 1
                if self.current_frame == len(self.animation):
                    self.current_frame = 0
        self.fps += 1
        if self.fps == 24:
            self.fps = 0
        return [self.current_sprite, self.location]

    def load_animations(self) \
            -> list:
        """
        :return: una lista con las animaciones de la imagen cargadas y ajustadas a la resolucion de la ventana
        """
        import os
        sprites_order = [f'dice_{sprite+1}' for sprite in range(len(os.listdir(self.path)))]
        sprites = []
        print(sprites_order)
        for sprite in range(len(sprites_order)):
            sprites.append(self.pygame.image.load(f'{Dice.path}/{sprites_order[sprite]}.png'))
        sprites = self.scaling(sprites)
        return sprites

    def scaling(self, sprites: list) \
            -> list:
        """
        :param sprites: lista de sprites para ajustar tamano
        :return: lista con las sprites ya asjustadas
        """
        resolution = self.get_resolution()
        size_to_scale = (resolution[0]/5,
                         resolution[1]/3.3)
        scaled_sprites = []
        for sprite in sprites:
            scaled_sprites.append(self.pygame.transform.scale(sprite, size_to_scale))
        return scaled_sprites

    @staticmethod
    def get_resolution() \
            -> tuple:
        """
        :return: tupla con las dimensiones de la ventana
        """
        from screeninfo import get_monitors
        screen = [monitor for monitor in get_monitors()]

        for primary_screen in screen:
            if primary_screen.is_primary:
                size_tup = (primary_screen.width - (primary_screen.width / 384),
                            primary_screen.height - (primary_screen.height / 13.5))
                return size_tup

    def trow(self):
        def custom_function(x):
            if x % 2 == 0 and 0 <= x <= 10:
                return x // 2 + 1
            else:
                return None
        if self.current_frame % 2 == 1:
            self.current_frame += 1
            if self.current_frame == len(self.animation):
                self.current_frame = 0
        if self.regulation == 6:
            print('wtf')
            self.regulation = 1
            self.stop = False
            print(self.current_frame)
        else:
            self.regulation = 6
            self.stop = True
            return custom_function(self.current_frame)
        return None

    @staticmethod
    def get_location() \
            -> tuple:
        """
        :return: tupla con la poscision del dado respecto a la ventana
        """
        resolution = Dice.get_resolution()
        dice_location = (resolution[0] / 40, resolution[1] / 8)
        return dice_location
