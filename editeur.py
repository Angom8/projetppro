# -*- coding: iso-8859-15 -*-

import pygame
import os
from pygame.locals import *
from Level import *


#compléter les imports !!!!#


def normal_text(texte, x, y, color, screen): 
    font_text = pygame.font.SysFont('roboto', 17)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))
    
def title_text(texte, x, y, color, screen): 
    font_text = pygame.font.SysFont('roboto', 33)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))

def conversion_tab(tab, i):

	y = 0
	while i >= len(tab):
		i -= len(tab)
		y += 1
	x = i
	
	return(x, y)	

def drawzoneEdition(taille):
	
	x, y = zoneEdit.get_size()
	
	edition = [[0]*len(taille[0])for _ in range(len(taille))]
	a = (220, 220, 220)
	b = (230, 230, 230)
	
	i = 0
	
	for c in range(len(taille)):
		for l in range(len(taille[c])):
		
			if(i==0):
				edition[c][l] = pygame.draw.rect(zoneEdit , a, (c*25, l*25, 25, 25))
				i += 1
			else:
				edition[c][l] = pygame.draw.rect(zoneEdit , b, (c*25, l*25, 25, 25))
				i -= 1
	
	return(edition)
	



def creerBloc(compteBloc, taille, edition, creation):
	
	font = pygame.font.SysFont('Consolas', 20)
	fini = False
	ok = False

	x, y = pygame.mouse.get_pos()
	for c in range(len(edition)):
		for l in range(len(edition[c])):
			collideTab = edition[c][l].collidepoint(x, y)
			collideCreation = creation.collidepoint(x, y)

			if collideTab:
				pressed = pygame.mouse.get_pressed()
				if pressed[0]:
					#on vérifie si la case est libre
					if taille[c][l] == 0:
						taille[c][l] == compteBloc
			
			if collideCreation:
				pressed = pygame.mouse.get_pressed()
				if pressed[0]:
					fini = True
					
									
	while fini==False:
		
		x, y = pygame.mouse.get_pos()
		for c in range(len(edition)):
			collideTab = edition[c][l].collidepoint(x, y)

			if collideTab:
				pressed = pygame.mouse.get_pressed()
				if pressed[0]:
					#on vérifie dans la "croix" de la case cliquée qu'il y a bien une case qui appartient déjà au bloc
					if c-1 > 0:
						if taille[c-1][l] == compteBloc:
							ok = True
					if c+1 < len(edition):
						if taille[c+1][l] == compteBloc:
							ok = True
					if l-1 > 0:
						if taille[c][l-1] == compteBloc:
							ok = True
					if l+1 < len(edition[c]):
						if taille[c][l+1] == compteBloc:
							ok = True
					
					#on vérifie si la case est libre et qu'il y a bien une case qui appartient déjà au bloc dans les environs
					if taille[c][l] == 0 and ok == True:
						taille[c][l] == compteBloc
					
					else:
						pygame.font.init()
						ecran.blit(font.render("Probleme, choissiez un autre bloc...", True, (0, 0, 0)), (4*largeur/10, 7.5*hauteur/10))




def editeur():
	FPS = 30
	pygame.init() 
	screen = pygame.display.set_mode((860, 640),HWSURFACE|DOUBLEBUF|RESIZABLE)
	
	pygame.display.set_caption("Place ton bloc ! - Editeur")
	pygame.display.set_icon(pygame.image.load("img/icone.png"))
	
	pygame.display.set_caption("Editeur")
	
	fond = pygame.image.load("img/background.jpg").convert()
	screen.blit(fond,(0,0))
	largeur, hauteur = pygame.display.get_surface().get_size()
	editeur = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))
	
	global zoneEdit
	zoneEdit = pygame.Surface((int(7.5*largeur/10), int(4*hauteur/10)))
	zoneEdit.fill((238, 238, 238))
	
	fleche = pygame.image.load("img/fleche.png").convert_alpha()
	fleche_rect = fleche.get_rect()
	
	bloc4 = pygame.draw.rect(screen, [185,250,255], pygame.Rect(int(largeur/9), hauteur/3, 30, 15))
	normal_text("4*4", int(largeur/9 + 7), hauteur/3 + 2, (0, 0, 0), screen)
	
	bloc5 = pygame.draw.rect(screen, [185,250,255], pygame.Rect(int(largeur/6), hauteur/3, 30, 15))
	normal_text("5*5", int(largeur/6 + 7), hauteur/3 + 2, (0, 0, 0), screen)
	
	bloc6 = pygame.draw.rect(screen, [185,250,255], pygame.Rect(int(largeur/4 - 25), hauteur/3, 30, 15))
	normal_text("6*6", int(largeur/4 - 18), hauteur/3 + 2, (0, 0, 0), screen)
	
	creation = pygame.draw.rect(screen, [255,54,54], pygame.Rect(int(8.75*largeur/10 - 90), 8.5*hauteur/10, 30, 15))
	normal_text("Creer bloc", int(8.75*largeur/10 - 90), 8.5*hauteur/10, (0, 0, 0), screen)
	
	terminer = pygame.draw.rect(screen, [255,54,54], pygame.Rect(int(8.75*largeur/10 - 90), 8.5*hauteur/10, 30, 15))
	normal_text("Terminer !", int(8.75*largeur/10 - 150), 8.5*hauteur/10, (0, 0, 0), screen)

	pygame.display.flip()
	clock = pygame.time.Clock()
    
	running = True
	compteBloc = 0
	nb = str(compteBloc)
	
	niveau = []
	edition = []
	
	while running:
	
		largeur, hauteur = pygame.display.get_surface().get_size()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type==VIDEORESIZE:
				screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
				screen.blit(pygame.transform.scale(fond,event.dict['size']),(0,0))
					
				
				
				
			if pygame.mouse.get_focused():
				x, y = pygame.mouse.get_pos()
				collide = fleche_rect.collidepoint(x, y)
		
				#bouton retour au menu
				if collide:
					pressed = pygame.mouse.get_pressed()
					if pressed[0]: 
						menu()
				
				
				collide4 = bloc4.collidepoint(x, y)
				collide5 = bloc5.collidepoint(x, y)
				collide6 = bloc6.collidepoint(x, y)
				
				
				#bouton choix 4*4
				if collide4:
					pressed = pygame.mouse.get_pressed()
					if pressed[0]:
						pygame.font.init()
						zoneEdit.fill((238, 238, 238))
						screen.blit(zoneEdit, (1.25*largeur/10,  4*hauteur/10))
						taille4 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
						edition = drawzoneEdition(taille4)
						creerBloc(compteBloc, taille4, edition, creation)
						pygame.font.quit()
						
				#bouton choix 5*5
				elif collide5:
					pressed = pygame.mouse.get_pressed()
					if pressed[0]:
						pygame.font.init()
						zoneEdit.fill((238, 238, 238))
						screen.blit(zoneEdit, (1.25*largeur/10,  4*hauteur/10))
						taille5 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
						edition = drawzoneEdition(taille5)
						creerBloc(compteBloc, taille5, edition, creation)
						pygame.font.quit()
								
				#bouton choix 6*6
				elif collide6:
					pressed = pygame.mouse.get_pressed()
					if pressed[0]:
						pygame.font.init()
						zoneEdit.fill((238, 238, 238))
						screen.blit(zoneEdit, (1.25*largeur/10,  4*hauteur/10))
						taille6 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
						edition = drawzoneEdition(taille6)
						creerBloc(compteBloc, taille6, edition, creation)
						
				

						
		if largeur > 400 or hauteur > 400:
			screen.blit(fleche, (0,0))
			pygame.font.init()
			
			editeur = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))
			
			title_text("Place ton bloc ! - Creez votre niveau :", largeur/7,hauteur/7, (0, 0, 0), screen)
			normal_text("Bloc numero : ", largeur/7,hauteur/7 + 60, (0, 0, 0), screen)
			
			zoneNbBlock = pygame.draw.rect(screen, (211, 242, 255), pygame.Rect(largeur/7 + 90, hauteur/7 + 50, largeur/20, hauteur/20))
			normal_text(nb, largeur/7 + 107, hauteur/7 + 60, (0, 0, 0), screen)
			
			creation = pygame.draw.rect(screen, [255,54,54], pygame.Rect(largeur/7 + 150, hauteur/7 + 60, 70, 20))
			normal_text("Creer bloc", largeur/7 + 158, hauteur/7 + 65, (0, 0, 0), screen)

			screen.blit(zoneEdit, (1.25*largeur/10,  4*hauteur/10))
	
			bloc4 = pygame.draw.rect(screen, [185,250,255], pygame.Rect(int(largeur/9), hauteur/3, 30, 15))
			normal_text("4*4", int(largeur/9 + 7), hauteur/3 + 2, (0, 0, 0), screen)
	
			bloc5 = pygame.draw.rect(screen, [185,250,255], pygame.Rect(int(largeur/6), hauteur/3, 30, 15))
			normal_text("5*5", int(largeur/6 + 7), hauteur/3 + 2, (0, 0, 0), screen)
	
			bloc6 = pygame.draw.rect(screen, [185,250,255], pygame.Rect(int(largeur/4 - 25), hauteur/3, 30, 15))
			normal_text("6*6", int(largeur/4 - 18), hauteur/3 + 2, (0, 0, 0), screen)
			
		else:
			pygame.font.init()
			normal_text("Merci d'agrandir la fenetre (mini 400*400)", 0,0, (255, 0, 0))
			
			
			
		
		
		
		
			
		
		clock.tick(FPS)
		pygame.display.flip()
		
		pygame.font.quit()
			
	pygame.quit()

editeur()