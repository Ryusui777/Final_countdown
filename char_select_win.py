import pygame
from screeninfo import get_monitors

class SelectWindow:
    def __init__(self):
        pygame.init()
        self.name = 'Start_Window'
        self.resolution = self.get_resolution()
        self.window_object = pygame.display.set_mode(self.resolution)
        self.window_object.fill((50, 50, 70))
        self.bg = pygame.image.load('Assets/bg/Select_screen.png')
        self.bg = pygame.transform.scale(self.bg, (self.resolution[0], self.resolution[1]))
        self.window_object.blit(self.bg, (0, 0))

    @staticmethod
    def get_resolution() -> tuple:
        screen = [monitor for monitor in get_monitors()]
        for primary_screen in screen:
            if primary_screen.is_primary:
                size_tup = (primary_screen.width - (primary_screen.width / 384),
                            primary_screen.height - (primary_screen.height / 13.5))
                return size_tup

    def selection_screen_pos(self, character_num: int) -> list:
        """
        :return: lista con las posiciones de los personajes en la pantalla
        de carga, en forma de tuple
        """
        resolution = self.get_resolution()
        y = 2
        match character_num:
            case 1:
                player_1 = (resolution[0] / 2, resolution[1] / y)
                return [player_1]
            case 2:
                player_1 = (resolution[0] / 3, resolution[1] / y)
                player_2 = (resolution[0] - resolution[0] / 3, resolution[1] / y)
                return [player_1, player_2]
            case 3:
                player_1 = (resolution[0] / 4, resolution[1] / y)
                player_2 = (resolution[0] / 2, resolution[1] / y)
                player_3 = (resolution[0] - resolution[0] / 4, resolution[1] / y)
                return [player_1, player_2, player_3]

    def put_characters_on(self, characters: list[pygame.Surface]) -> None:
        characters_pos = None
        match len(characters):
            case 1:
                characters_pos = self.selection_screen_pos(1)
            case 2:
                characters_pos = self.selection_screen_pos(2)
            case 3:
                characters_pos = self.selection_screen_pos(3)

        for character in range(len(characters)):
            round_x = characters_pos[character][0]
            round_y = characters_pos[character][1]
            character_rect = self.make_rects(characters[character], (round_x, round_y))
            self.window_object.blit(characters[character], character_rect)

    def make_rects(self, character: pygame.Surface, position: tuple) -> pygame.Rect:
        resolution = self.get_resolution()
        character_rect = character.get_rect()
        bg_rect = pygame.Rect(0, 0, resolution[0] / 4.8, resolution[1] / 1.7)
        bg_rect.center = position
        character_rect.center = position
        character_rect.bottom = bg_rect.bottom - bg_rect.bottom / 10
        pygame.draw.rect(self.window_object, (50, 250, 30), bg_rect)
        return character_rect

    def refresh(self, characters: list) -> None:
        self.window_object.fill((50, 50, 70))
        self.window_object.blit(self.bg, (0, 0))
        self.put_characters_on(characters)
        pygame.display.update()
