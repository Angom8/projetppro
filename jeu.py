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
    blocs = []
    blocs.append(creerBloc(i, niveau))
    
    while check == False:
    	
    	if i != 1 : 
    		blocs.append(creerBloc(i, niveau))#valeur de la case
    		
    	g = 0
    	h = 0
    	checkdeux = False
    	
    	i+=1
    	
    	while g	< len(niveau.getPosition()):#verifie si lon cree encore des blocs ou pas
    		while h	< len(niveau.getPosition()[g]) and checkdeux != True :
    			if str(i) == niveau.getPosition()[g][h] :
    				checkdeux = True
    			h+=1
    		h = 0
    		
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

    return leBloc	
    		
def drawBloc(x, y, leBloc, t):

    r = lambda: random.randint(0,255)
    a = (r(),r(),r())
    for l in range(len(leBloc)):
        for c in range(len(leBloc[0])):
        	if leBloc[l][c] != 0:
        		pygame.draw.rect(SURFACE , a, (x+ (c*t), y+(l*t), t, t))

def drawBlocs(u, v, niveau):

    t = (u*v)
    blocs = creerBlocs(niveau)
    t = t/(len(blocs))
    print str(blocs)
    c = 0
    x = t
    y = t
    random.shuffle(blocs)
    for c in range(len(blocs)):
    	
    	if(x>u):
    		y += t
    		
    	drawBloc(x, y, blocs[c], t)
    	x +=  t
    	
pygame.init()
ecran = pygame.display.set_mode((640,480),HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption("Place ton bloc ! - ")
pygame.display.set_icon(pygame.image.load("img/icone.png"))
fond = pygame.image.load("img/background.jpg").convert()
largeur, hauteur = pygame.display.get_surface().get_size()
ecran.blit(fond,(0,0))
SURFACE = pygame.display.set_mode((largeur, hauteur))
running = True
drawBlocs(((2*largeur)/100), ((2*hauteur)/100), lecture("levels/Test.lvl"))
while running:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
		running = False
