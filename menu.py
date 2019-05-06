# -*- coding: iso-8859-15 -*-
import pygame
import os
from lecture import *
from pygame.locals import *

def normal_text(texte, x, y, color): 
    font_text = pygame.font.SysFont('roboto', 17)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))
    
def title_text(texte, x, y, color): 
    font_text = pygame.font.SysFont('roboto', 33)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))

def fileremove(niveau):#uniquement custom
    os.remove("levels/" + niveau.getNom() + ".lvl")
    removeniveau(niveau)
  
def affichageniveau(niveau, x, y):#le nom + bouton play
    t, h = pygame.display.get_surface().get_size()
    normal_text(niveau.getNom(), x,y, (0, 0, 0))
    panel = pygame.draw.rect(screen, [64,164,151], pygame.Rect(int(x+ 2*t/3), y, 30, 15))
    normal_text("Play", x + int(2*t/3 + 5), y, (0, 0, 0))
    retour = [niveau, panel, 1, 1]
    return(retour)
  
def affichageniveaucustom(niveau, x, y):#le nom + boutons play, edit et delete
    t, h = pygame.display.get_surface().get_size()
    normal_text(niveau.getNom(), x,y, (0, 0, 0))
    suppr = pygame.draw.rect(screen, [255,0,0], pygame.Rect(int(x+ 2*t/3-10), y, 40, 15))
    normal_text("Delete", x + int(2*t/3 -5), y, (0, 0, 0))
    edit = pygame.draw.rect(screen, [189,191,38], pygame.Rect(int(x+ 2*t/3 - 40), y, 30, 15))
    normal_text("Edit", x + int(2*t/3 + 5 - 40), y, (0, 0, 0))
    play = pygame.draw.rect(screen, [64,164,151], pygame.Rect(int(x+ 2*t/3 - 70), y, 30, 15))
    normal_text("Play", x + int(2*t/3 + 5 - 70), y, (0, 0, 0))
    retour = [niveau, play, edit, suppr]
    return(retour)
    
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
niveau = []

while running:
	
    largeur, hauteur = pygame.display.get_surface().get_size()
    
    if largeur > 400 or hauteur > 400:#sinon affichage pas bon
	fond = pygame.image.load("img/background.jpg").convert()
    	screen.blit(fond,(0,0))
   	menu = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))
    	for event in pygame.event.get():
        	if event.type == pygame.QUIT:
			running = False
      	 	elif event.type==VIDEORESIZE:
			screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
			screen.blit(pygame.transform.scale(fond,event.dict['size']),(0,0))
		
   	if pygame.mouse.get_focused():
        	x , y = pygame.mouse.get_pos()

		for c in range(len(niveau)):
			collide = niveau[c][1].collidepoint(x, y)
			if collide:
        			pressed = pygame.mouse.get_pressed()
        			if pressed[0]:
            				print "Opening ... " + niveau[c][0].getNom()
					jeu(niveau[c][0]) 
                		
       		c = 0
       	
       		while c < len(niveau):
       			if niveau[c][2] != 1:
				collide = niveau[c][2].collidepoint(x, y)
				if collide:
        				pressed = pygame.mouse.get_pressed()
        				if pressed[0]:
            					print "Editing ... " + niveau[c][0].getNom()
						editeur(niveau[c][0])
				collide = niveau[c][3].collidepoint(x, y)
				if collide:
        				pressed = pygame.mouse.get_pressed()
        				if pressed[0]:
            					print "Deleting ... " + niveau[c][0].getNom()
						fileremove(niveau[c][0])
			c+=1
		
	
   	menu = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))	
    	pygame.font.init
    	title_text("Place ton bloc ! - Choisissez votre niveau :", largeur/7,hauteur/7, (0, 0, 0))
    	normal_text("Niveaux standards :", largeur/7,hauteur/7 + 30, (0, 0, 0))
    
    
    	niveau.append(affichageniveau(lecture("baselevels/Niveau1.lvl"), largeur/7, hauteur/7 + 60))
    	niveau.append(affichageniveau(lecture("baselevels/Niveau2.lvl"), largeur/7, hauteur/7 + 80))
    	niveau.append(affichageniveau(lecture("baselevels/Niveau3.lvl"), largeur/7, hauteur/7 + 100))
	niveau.append(affichageniveau(lecture("baselevels/Niveau4.lvl"), largeur/7, hauteur/7 + 120))
	niveau.append(affichageniveau(lecture("baselevels/Niveau5.lvl"), largeur/7, hauteur/7 + 140))
    
    	normal_text("Niveaux standards :", largeur/7,hauteur/7 + 170, (0, 0, 0))
    
   	liste = os.listdir('levels/')
	inter = 200
	    
    	for d in range(len(liste)):
    		if str(liste[d][len(liste[d])-4:len(liste[d])]) == ".lvl":	
    			niveau.append(affichageniveaucustom(lecture("levels/" + liste[d]), largeur/7, hauteur/7 + 200 + d*30))
    
    
    	pygame.font.quit
    	
    else:
    	pygame.font.init
    	normal_text("Merci d'agrandir la fenetre (mini 400*400)", 0,0, (255, 0, 0))
    	pygame.font.quit
    	for event in pygame.event.get():
        	if event.type == pygame.QUIT:
			running = False
      	 	elif event.type==VIDEORESIZE:
			screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
			screen.blit(pygame.transform.scale(fond,event.dict['size']),(0,0))
    
    clock.tick(FPS)
    pygame.display.flip()
    
pygame.quit()


