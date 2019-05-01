
import pygame
from pygame.locals import *

def normal_text(texte, x, y, color): 
    font_text = pygame.font.SysFont('roboto', 17)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))
def title_text(texte, x, y, color): 
    font_text = pygame.font.SysFont('roboto', 35)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))

FPS = 30

pygame.init()
screen = pygame.display.set_mode((640,480),HWSURFACE|DOUBLEBUF|RESIZABLE)

pygame.display.set_caption("Place ton bloc ! - Menu")
pygame.display.set_icon(pygame.image.load("img/icone.png"))

fond = pygame.image.load("img/background.jpg").convert()
screen.blit(fond,(0,0))
largeur, hauteur = pygame.display.get_surface().get_size()
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))

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
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))	
    pygame.font.init
    title_text("Place ton bloc ! - Choisissez votre niveau :", largeur/7,hauteur/7, (0, 0, 0))
    pygame.font.quit
    
    
    
    
    
    
    
    
    
    clock.tick(FPS)
    pygame.display.flip()
    
pygame.quit()



