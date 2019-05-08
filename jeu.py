# -*- coding: iso-8859-15 -*-
import pygame
import os
from lecture import *
from pygame.locals import *
from menu import *
import random
import time

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
    pygame.font.init()
    global ecran
    ecran = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Place ton bloc ! - " + niveau.getNom())
    pygame.display.set_icon(pygame.image.load("img/icone.png"))
    fond = pygame.image.load("img/background.jpg").convert()
    ecran.blit(fond,(0,0))
    largeur, hauteur = pygame.display.get_surface().get_size()
    
    global zoneblocs, zonejeu
    
    zoneblocs = pygame.Surface((int(7.5*largeur/10), int(2.5*hauteur/10)))
    pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))
    pygame.display.flip()
    
    clock = pygame.time.Clock()
    counter, text = 180, '180'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    running = True
    bloc_graging = False
	
    zglobal = pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))

    zoneblocs = pygame.Surface((int(7.5*largeur/10), int(2.5*hauteur/10)))
   	
    zoneblocs.fill((245, 245, 245))
   	
    blocs = drawBlocs(14*largeur/10, 1.25*hauteur/10, niveau)

    ecran.blit(zoneblocs, (1.25*largeur/10,  1.25*hauteur/10))
    	
    zonejeu = pygame.Surface((int(7.5*largeur/10), int(4*hauteur/10)))
    zonejeu.fill((245, 245, 245))
    ecran.blit(zonejeu, (1.25*largeur/10,  4*hauteur/10))
   	
    termine = pygame.draw.rect(ecran, [64,164,151], pygame.Rect(int(8.75*largeur/10 - 48), 8.5*hauteur/10, 48, 15))
    normal_text("Terminer", int(8.75*largeur/10 - 49), 8.5*hauteur/10, (0, 0, 0), ecran)	

    play = pygame.draw.rect(ecran, [64,164,151], pygame.Rect(int(8.75*largeur/10 - 90), 8.5*hauteur/10, 30, 15))
    normal_text("Play", int(8.75*largeur/10 + 5 - 90), 8.5*hauteur/10, (0, 0, 0), ecran)
    
    tab = [[0] * len(niveau.getPosition()[0]) for _ in range(len(niveau.getPosition()))]
    enjeu= False
    
    while running:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			running = False
		if event.type == pygame.USEREVENT and enjeu == True: 
            			counter -= 1
           			text = str(counter).rjust(3)
		if pygame.mouse.get_focused():
        			x , y = pygame.mouse.get_pos()

				collide = play.collidepoint(x, y)
				if collide:

       				## Détecte les clique de souris.
        				pressed = pygame.mouse.get_pressed()
        				if pressed[0]: # 0=gauche, 1=milieu, 2=droite
        					jeuencours = drawzonejeu(niveau)
            					enjeu = True
            			collide = termine.collidepoint(x, y)
				if collide:

       				## Détecte les clique de souris.
        				pressed = pygame.mouse.get_pressed()
        				if pressed[0]: # 0=gauche, 1=milieu, 2=droite
            					if estTermine:
            						if (counter + niveau.getRang(3)) < 180:            						
            							addsave(niveau, 3)
            						elif (counter + niveau.getRang(2)) < 180:
            							addsave(niveau, 2)
            						elif (counter + niveau.getRang(1)) < 180:
            							addsave(niveau, 1)
            						menu()

       	
	
  	largeur, hauteur = pygame.display.get_surface().get_size()
  	font = pygame.font.SysFont('Consolas', 20)
  	fondtimer = pygame.Surface((int(0.5*largeur/10), int(0.5*hauteur/10)))
  	fondtimer.fill((255,255,255))
  	ecran.blit(fondtimer, (1.25*largeur/10,  8.5*hauteur/10))
   	ecran.blit(font.render(text, True, (0, 0, 0)), (1.25*largeur/10, 8.5*hauteur/10))
   	
   	if enjeu == True:
   		jeuencours = drawzonejeu(niveau)
   		ecran.blit(zonejeu, (1.25*largeur/10,  4*hauteur/10))
   	
   	
   	
   	
        clock.tick(FPS)
        del font
        pygame.display.flip()
    pygame.font.quit() 
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
        		zebloc = pygame.draw.rect(zoneblocs , a, (x+ (c*25), y+(l*25), 25, 25))
    return zebloc    		

def drawBlocs(u, v, niveau):

    t = (v)
    blocs = creerBlocs(niveau)
    retour = []
    t = t/(len(blocs))
    c = 0
    x = t
    y = t
    random.shuffle(blocs)
    for c in range(len(blocs)):
    	
    	if(x>u):
    		y += t
    		
    	retour.append(drawBloc(x, y, blocs[c], t))
    	x +=  t
    	
    return(retour)
    
def drawzonejeu(niveau):


    x, y = zonejeu.get_size()
    	
    jeuencours = []
    a = (220, 220, 220)
    b = (230, 230, 230)
    
    i = 2
    
    for c in range(len(niveau.getPosition())):
    
    	for l in range(len(niveau.getPosition())):
    	
    		if(i%2!=0):
   			jeuencours.append(pygame.draw.rect(zonejeu , a, (c*25, l*25, 25, 25)))
   		else:
   			jeuencours.append(pygame.draw.rect(zonejeu , b, (c*25, l*25, 25, 25)))
   		i+=1
   			
    return(jeuencours)
    
def estTermine(tab, niveau):
	i = 0
	j = 0
	verif = True
	
	while i < len(tab) and verif == True:
		while j < len(tab[i]):
			if tab[i][j] != niveau.getPosition()[i][j]:
				verif = False
			else:
				i += 1
				j +=1
	
	return verif
