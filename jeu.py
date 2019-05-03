# -*- coding: iso-8859-15 -*-
import pygame
import os
from lecture import *
from pygame.locals import *
import random

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
    SURFACE = pygame.display.set_mode((largeur, hauteur))
    clock = pygame.time.Clock()
    running = True
    bloc_graging = False
    while running:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			running = False
    		elif event.type==VIDEORESIZE:
			ecran=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
			ecran.blit(pygame.transform.scale(fond,event.dict['size']),(0,0))
		elif event.type == pygame.MOUSEBUTTONDOWN:
           		if event.button == 1:            
               			if rectangle.collidepoint(event.pos):
                   			bloc_draging = True
                    			mouse_x, mouse_y = event.pos
                    			offset_x = rectangle.x - mouse_x
                    			offset_y = rectangle.y - mouse_y

       		elif event.type == pygame.MOUSEMOTION:
            		if bloc_draging:
               			mouse_x, mouse_y = event.pos
                		bloc.x = mouse_x + offset_x
                		bloc.y = mouse_y + offset_y

  	largeur, hauteur = pygame.display.get_surface().get_size()
   	pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))	
   	pygame.font.init
        title_text("Place ton bloc ! - Choisissez votre niveau :", largeur/7,hauteur/7, (0, 0, 0), ecran)
        pygame.font.quit
    
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
    
def creerBlocs(niveau):

    i = 1
    check = False
    while check == False:
    	
    	blocs = []
    	blocs.append(creerBloc(i, niveau))#valeur de la case
    	
    	g = 0
    	h = 0
    	checkdeux = False
    	
    	while g	< len(niveau.getPosition()):#verifie si lon cree encore des blocs ou pas
    		while h	< len(niveau.getPosition()[g]) and checkdeux != True :
    			if i == niveau.getPosition()[g][h] :
    				checkdeux = True
    			i+=1
    			h+=1
    		
    		g+=1
    	
    	
    	if checkdeux == False:
    		check = True
    
    return(blocs) #tous les blocs
        
def creerBloc(i, niveau):

    positions =  niveau.getPosition()
    leBloc = [[0] * len(positions[0]) for _ in range(len(positions))]
    l = 0
    c = 0
    
    while l < len(positions) :
    	while c < len(positions[l]) :
		if positions[l][c] == str(i):
			leBloc[l][c] = i
		c += 1		
	l+= 1	
	c = 0

    print str(leBloc)
    return leBloc	
    		
def drawPiece(x, y, leBloc):

    r = lambda: random.randint(0,255)
    a = (r(),r(),r())
    for l in range(len(leBloc)):
        for c in range(len(leBloc[0])):
        	if leBloc[l][c]:
        		pygame.draw.rect(SURFACE, a, (c*50, l*50, 50, 50))


    
print str(lecture("levels/Test.lvl").getPosition())
blocs = creerBlocs(lecture("levels/Test.lvl"))	
pygame.init()
ecran = pygame.display.set_mode((640,480),HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption("Place ton bloc ! - ")
pygame.display.set_icon(pygame.image.load("img/icone.png"))
fond = pygame.image.load("img/background.jpg").convert()
largeur, hauteur = pygame.display.get_surface().get_size()
ecran.blit(fond,(0,0))
SURFACE = pygame.display.set_mode((largeur, hauteur))
running = True
drawPiece(100, 100, blocs[0])
while running:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    	    running = False
    	
