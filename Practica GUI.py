
import pygame
import time 
import random

WIDHT, HEIGHT= 600,600
WIN= pygame.display.set_mode((WIDHT, HEIGHT))

pygame.display.set_caption("Serpientes y Escaleras")

BG=pygame.transform.scale(pygame.image.load("BG.jpg"), (WIDHT, HEIGHT))

Player_widht= 40
Player_height= 40
Player_velocity= 0.6

Player2_widht= 40
Player2_height= 40
Player2_velocity= 0.6


def draw(player, player2):
    WIN.blit(BG, (0,0))

    pygame.draw.rect(WIN, "white", player)
    pygame.draw.rect(WIN, "black", player2)
    pygame.display.update()


def main():
    run=True
    
    player=pygame.Rect(65, HEIGHT-Player_height, 
                       Player_widht, Player_height)
    player2=pygame.Rect(120, HEIGHT-Player2_height, 
                       Player2_widht, Player2_height)
    
    
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: 
            player.x -= Player_velocity 
        if keys[pygame.K_RIGHT] :
            player.x += Player_velocity 
        if keys[pygame.K_UP]: 
            player.y -= Player_velocity 
        if keys[pygame.K_DOWN]:
            player.y += Player_velocity 


        keys2 = pygame.key.get_pressed()
        if keys2[pygame.K_a]: 
            player2.x -= Player2_velocity 
        if keys2[pygame.K_d]:
            player2.x += Player2_velocity 
        if keys2[pygame.K_w]: 
            player2.y -= Player2_velocity 
        if keys2[pygame.K_s]:
            player2.y += Player2_velocity 
    
       
        draw(player, player2)
        

        


    pygame.quit()

if __name__=="__main__":
    main()
