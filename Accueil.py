# -*- coding: iso-8859-15 -*-
import pygame
import os
from pygame.locals import *
from math import sin
from menu import *
import time

#init + fond
FPS = 30
pygame.init()
fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("img/background.jpg").convert()
fenetre.blit(fond, (0,0))

#fenetre globale
pygame.display.set_caption("Demarrage")
pygame.display.set_icon(pygame.image.load("img/icone.png"))
logo = pygame.image.load("img/URCA.png").convert_alpha()

texte = "THEBAULT Antoine / ALEXANDRE Clement"
font = pygame.font.SysFont('roboto', 20)
pygame.mixer.music.load("sons/intro.mp3")

#timer
counter, text = 8, '180'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.display.flip()
clock = pygame.time.Clock()  
		
for event in pygame.event.get():
	if event.type == pygame.USEREVENT: #decrementation du timer
		counter -= 1
		text = str(counter).rjust(3) if counter > 0 else pygame.quit()
	
#recuperation taille fenetre		
largeur, hauteur = pygame.display.get_surface().get_size()
	
#lecture du son + presentation logo
pygame.mixer.music.play()
fenetre.blit(logo, ((largeur/2) - 65, hauteur*0.40))
pygame.display.flip()
pygame.time.wait(4000)
	
#les noms
fenetre.blit(fond , (0,0))
fenetre.blit(font.render(texte, True, (0, 0, 0)), ((largeur/5+65) , hauteur*0.5))
pygame.display.flip()
pygame.time.wait(3000)
	
#fin son
pygame.mixer.music.stop()
	
clock.tick(FPS)
	
menu()
print "Extinction du jeu..."		
pygame.quit()
