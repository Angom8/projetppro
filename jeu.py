# -*- coding: iso-8859-15 -*-

import pygame
import os
from lecture import *
from pygame.locals import *

def normal_text(texte, x, y, color, ecran): 
    font_text = pygame.font.SysFont('roboto', 17)
    affichage = font_text.render(texte, 1, (color))
    ecran.blit(affichage,(x,y))
    
def title_text(texte, x, y, color, ecran): 
    font_text = pygame.font.SysFont('roboto', 35)
    affichage = font_text.render(texte, 1, (color))
    ecran.blit(affichage,(x,y))

def initialisation(niveau):
    input = [[-1]*len(niveau.getPosition()[0])]
    
def jeu(niveau):
    FPS = 30
    pygame.init()
    ecran = pygame.display.set_mode((640,480),HWSURFACE|DOUBLEBUF|RESIZABLE)
    pygame.display.set_caption("Place ton bloc ! - " + niveau.getNom())
    pygame.display.set_icon(pygame.image.load("img/icone.png"))
    fond = pygame.image.load("img/background.jpg").convert()
    ecran.blit(fond,(0,0))
    largeur, hauteur = pygame.display.get_surface().get_size()
    pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))
    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    while running:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			running = False
    		elif event.type==VIDEORESIZE:
			ecran=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
			ecran.blit(pygame.transform.scale(fond,event.dict['size']),(0,0))
		
  	largeur, hauteur = pygame.display.get_surface().get_size()
   	pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))	
   	pygame.font.init
        title_text("Place ton bloc ! - Choisissez votre niveau :", largeur/7,hauteur/7, (0, 0, 0), ecran)
        pygame.font.quit
    
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


def estTermine(tab, niveau):
	i = 0
	j = 0
	verif = True
	
	while i < len(tab) and verif == True
		while j < len(tab[i])
			if tab[i][j] != niveau.getPosition()[i][j]
				verif = False
			else 
				i += 1
				j +=1
	
	
	if verif == True
		terminer()	
	
	return verif

def creerBlocs(niveau):

    i = 1
    check = False
    while check == False:
    	
    	Blocs = []
    	Blocs.append(creerBloc(i, niveau))#valeur de la case
    	
    	g = 0
    	h = 0
    	checkdeux = False
    	
    	while g	< len(niveau.getPosition()):#verifie si lon cree encore des blocs ou pas
    		while h	< len(niveau.getPosition()[g]) and check!= True :
    			if i == niveau.getPosition()[h] :
    				checkdeux = True
    			
    			h+=1
    		
    		g+=1
    	
    	
    	if checkdeux == False:
    		check = True
    
    return(Blocs, i) #retourne le max i et tous les blocs
        
def creerBloc(i, niveau):
    
    leBloc = [[0]*len(niveau.getPosition())]*len(niveau.getPosition()[0])
   
    positions =  niveau.getPosition()
    for l in range(len(positions)) :
	for c in range(len(positions[l])) :
		if positions[l][c] == str(i):
			leBloc[l][c] = i
			
    print str(leBloc)
    return leBloc			
