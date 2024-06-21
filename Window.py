class Window:
    import pygame

    def __init__(self):
        import pygame
        self.pygame.init()
        self.resolution = self.get_resolution()  # Es la reoslucion de laventana
        self.window_object = pygame.display.set_mode(self.resolution)  # Crea el objeto de la ventana
        self.bg_color = (48, 25, 52)  # color  base de la ventana
        self.bg = self.prepare_bg('Assets/bg/In_game_bg.png')  # Carga el bg

    def prepare_bg(self, bg_image: str) \
            -> pygame.Surface:
        """
        :param bg_image: El path hacia la imagen del bg
        :return: imagen cargada y ajustada del bg
        """
        resolution = Window.get_resolution()
        bg_image_load = self.pygame.image.load(bg_image)
        bg = self.pygame.transform.scale(bg_image_load, (resolution[0] / 1.335, resolution[1]))
        self.window_object.fill(self.bg_color)
        return bg

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

    def refresh(self, characters: list, items: list) \
            -> None:
        """
        :param characters: lista de los personajes para poner en pantalla
        :param items: lista de items para poner en pantalla
        """
        self.window_object.blit(self.bg, (self.resolution[0] / 4, 0))
        self.put_items_on(items)
        self.put_characters_on(characters)
        self.pygame.display.update()

    def put_items_on(self, items: list) \
            -> None:
        for item in items:
            self.window_object.blit(item[0], item[1])

    def put_characters_on(self, characters: list) \
            -> None:
        for character in characters:
            self.window_object.blit(character[0], character[1])


if __name__ == '__main__':
    import pygame
    import Dice

    win = Window()
    dice = Dice.Dice()
    run = 1
    clock = pygame.time.Clock()
    while run:
        clock.tick(24)
        print_dice = dice.give_frame()
        lista_on_screen = [print_dice]
        win.refresh([], lista_on_screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
