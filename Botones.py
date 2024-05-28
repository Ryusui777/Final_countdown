import pygame
import sys

pygame.init()

width, hight= 900, 900
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption("Boton")
main_font = pygame.font.SysFont("cambria", 60)

class Button(): 
    def __init__ (self, image, x_pos, y_pos, text_input):
        self.image= image
        self.x_pos= x_pos
        self.y_pos= y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input,True, "White")
        self.text_rect= self.text.get_rect(center=(self.x_pos, self.y_pos))
       
    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def verificarInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
         print("Boton presionado")
    
    def cambiarColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
            self.text= main_font.render(self.text_input,True, "purple")
        else:
            self.text= main_font.render(self.text_input,True, "white")


SuperficieBoton= pygame.image.load("buttons.png")
SuperficieBoton=pygame.transform.scale(SuperficieBoton,(300, 100))

Boton= Button(SuperficieBoton,450, 450, "Start")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Boton.verificarInput(pygame.mouse.get_pos())
    
    screen.fill("Blue")
    Boton.update()
    Boton.cambiarColor(pygame.mouse.get_pos())
    pygame.display.update()
