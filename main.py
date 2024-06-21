
class GameManager:
    import pygame
    import Window
    import Player
    import Dice
    import char_select_win
    import Enemies
    pygame.init()

    def __init__(self):

        self.ps_ongoing = False
        self.ps = None
        self.ps_args = []
        self.player_turn = 0
        self.players = []
        self.running = True
        self.clock = self.pygame.time.Clock()

    def main_game(self):

        player_1 = self.Player.Player()
        dice = self.Dice.Dice()
        win = self.Window.Window()
        players = [player_1]
        enemies = self.Enemies.Enemies()
        while self.running:
            self.clock.tick(24)
            players_frame = [player_1.give_frame()]
            items = [dice.give_frame()]
            win.refresh(characters=players_frame, items=items)

            self.event_manager(players, dice, [])
            print('hello my life hello')

    def character_selection(self):
        run = True
        win = self.char_select_win.SelectWindow()
        player_1 = self.Player.Player()
        players = [player_1]
        clock = self.pygame.time.Clock()
        while run:
            clock.tick(24)
            loaded_players = []
            for player in players:
                loaded_players.append(player.selection_character_give_frame())
            win.refresh(loaded_players)

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    run = False
                    break

    def checking_characther_enemies(self):
       pass


    def trowing_dice(self, dice: Dice.Dice):
        tiro = dice.trow()
        return tiro

    def event_manager(self, players: list[Player.Player], dice: Dice.Dice, enemies: list):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.running = False
                break
            if event.type == self.pygame.KEYDOWN and not self.ps_ongoing:
                if event.key == self.pygame.K_SPACE:
                    trow = self.trowing_dice(dice)
                    if trow is not None:
                        self.ps = 'moving_player'
                        self.ps_args = [trow]
                        self.ps_ongoing = True
                if event.key == 104:
                    pass

        if self.ps_ongoing:
            match self.ps:
                case 'moving_player':
                    moving_done = self.moving_player(self.ps_args, players[self.player_turn])
                    if moving_done:
                        self.ps_ongoing = False
                        self.change_player_turn()

    def  select_sreen_manager(self):
        pass

    def change_player_turn(self):
        self.player_turn += 1
        if self.player_turn >= len(self.players):
            self.player_turn = 0


    def moving_player(self, spaces, player) -> bool:
        done_moving = player.moving(spaces)
        return done_moving





if __name__ == '__main__':
    Game = GameManager()
    Game.main_game()
