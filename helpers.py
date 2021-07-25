import pygame

pygame.init()

def drawHitBox(x,y,img,screen):
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x, y, img.get_width(), img.get_height()), 2)


    
        