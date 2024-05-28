import pygame 
import sys 

width, hight= 600, 600
FPS= 60 

class game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, hight))
        pygame.display.set_caption("Mario Bros")
        self.clock = pygame.time.Clock()

        self.GSM = GSM("Start")
        self.start=start(self.screen, GSM)
        self.level=level(self.screen, GSM)

        self.sates={"Start": self.start, "Level": self.level }

    def run(self):
        while True:
            for repeticion in pygame.event.get():
                if repeticion.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if repeticion.type == pygame.KEYDOWN:
                    self.GSM.set_state("Level")

            self.sates[self.GSM.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)
        
class start:
    
    def __init__(self,display,GSM):
        self.display= display
        self.GSM = GSM
        self.BG=pygame.transform.scale(pygame.image.load("BranyDavid.jpg"), (width, hight))

    def run(self):
        self.display.blit(self.BG, (0, 0))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.GSM.set_state("Level")

class level:
    def __init__(self,display,GSM):
        self.display= display
        self.GSM = GSM
        self.BG=pygame.transform.scale(pygame.image.load("MB.jpg"), (width, hight))

    def run(self):
        self.display.blit(self.BG, (0, 0))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.GSM.set_state("Start") 

class GSM:
    def __init__(self,curentState):
        self.curentState = curentState
    def get_state(self):
        return self.curentState
    def set_state(self,state):
        self.curentState = state

if __name__=="__main__":
    Game = game()
    Game.run()
    