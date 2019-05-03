# -*- coding: iso-8859-15 -*-
import pygame
import os
from lecture import *
from pygame.locals import *

def normal_text(texte, x, y, color): 
    font_text = pygame.font.SysFont('roboto.ttf', 17)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))
    
def title_text(texte, x, y, color): 
    font_text = pygame.font.SysFont('roboto.ttf', 33)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))

def fileremove(niveau):#uniquement custom
    os.remove("levels/" + niveau.getNom() + ".lvl")
    removeniveau(niveau)
  
def affichageniveau(niveau, x, y):
    t, h = pygame.display.get_surface().get_size()
    normal_text(niveau.getNom(), x,y, (0, 0, 0))
    pygame.draw.rect(screen, [255,0,0], pygame.Rect(int(x+ 2*t/3), y, 30, 15))
    normal_text("Play", x + int(2*t/3 + 5), y, (0, 0, 0))
    return(niveau, x, y)
  
def affichageniveaucustom(niveau):
    pygame.font.init
    title_text(niveau.getNom())
    pygame.font.quit
    
FPS = 30

pygame.init()
screen = pygame.display.set_mode((640,480),HWSURFACE|DOUBLEBUF|RESIZABLE)

pygame.display.set_caption("Place ton bloc ! - Menu")
pygame.display.set_icon(pygame.image.load("img/icone.png"))

fond = pygame.image.load("img/background.jpg").convert()
screen.blit(fond,(0,0))
largeur, hauteur = pygame.display.get_surface().get_size()
menu = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))

pygame.display.flip()
clock = pygame.time.Clock()

default = os.listdir('baselevels/')
i = 0
defaultlevels = [0]*len(default)

for i in range (len(default)):
	defaultlevels[i] = lecture("baselevels/" + str(default[i]))

running = True

while running:

    niveau = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
		running = False
        elif event.type==VIDEORESIZE:
		screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
		screen.blit(pygame.transform.scale(fond,event.dict['size']),(0,0))
	elif event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()   # the x and y coordinates of the cursor position where the mouse was clicked
                	
           	for c in range(len(niveau)):
			if niveau[c][1] <= x and x <= (niveau[c][1]+30) and niveau[c][2] <= y and y <= (niveau[c][1]+15):
				print "Hello"
				jeu(niveau[c][0])
		
    largeur, hauteur = pygame.display.get_surface().get_size()
    menu = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))	
    pygame.font.init
    title_text("Place ton bloc ! - Choisissez votre niveau :", largeur/7,hauteur/7, (0, 0, 0))
    normal_text("Niveaux standards :", largeur/7,hauteur/7 + 30, (0, 0, 0))
    
    
    niveau.append(affichageniveau(lecture("baselevels/Niveau1.lvl"), largeur/7, hauteur/7 + 60))
    niveau.append(affichageniveau(lecture("baselevels/Niveau2.lvl"), largeur/7, hauteur/7 + 80))
    niveau.append(affichageniveau(lecture("baselevels/Niveau3.lvl"), largeur/7, hauteur/7 + 100))
    niveau.append(affichageniveau(lecture("baselevels/Niveau4.lvl"), largeur/7, hauteur/7 + 120))
    niveau.append(affichageniveau(lecture("baselevels/Niveau5.lvl"), largeur/7, hauteur/7 + 140))
    
    pygame.font.quit
    
    clock.tick(FPS)
    pygame.display.flip()
    
pygame.quit()


