import pygame
from pygame.locals import *

FPS = 30

pygame.init()
screen = pygame.display.set_mode((640,480),HWSURFACE|DOUBLEBUF|RESIZABLE)

pygame.display.set_caption("Place ton bloc ! - Menu")
fond = pygame.image.load("img/background.jpg").convert()
screen.blit(fond,(0,0))
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100,100, 200, 200))

pygame.display.flip()
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
		running = False
        elif event.type==VIDEORESIZE:
		screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
		screen.blit(pygame.transform.scale(fond,event.dict['size']),(0,0))
		largeur, hauteur = pygame.display.get_surface().get_size()
		pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100,100, largeur/2, hauteur/2))

    clock.tick(FPS)
    pygame.display.flip()
    print str(pygame.display.get_surface())
    
pygame.quit()
