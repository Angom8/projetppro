# -*- coding: iso-8859-15 -*-

import pygame
import os
from pygame.locals import *
from Level import *
from menu import *
from save import *

def editeur():

	#initialisation
	global zoneEdit, screen, edition, niveau, compteBloc
	firstBloc = True
	FPS = 30
	pygame.init() 
	running = True
	r = lambda: random.randint(0,255)
	compteBloc = [(r(),r(),r())]
	nb = str(len(compteBloc))
		
	screen = pygame.display.set_mode((600,600))	
	pygame.display.set_caption("Place ton bloc ! - Editeur")
	pygame.display.set_icon(pygame.image.load("img/icone.png"))
	pygame.display.set_caption("Editeur")
	
	#fond (premier appel)
	fond = pygame.image.load("img/background.jpg").convert()
	screen.blit(fond,(0,0))
	largeur, hauteur = pygame.display.get_surface().get_size()
	editeur = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))
	
	#Zone d'édition (premier appel)
	zoneEdit = pygame.Surface((int(7.5*largeur/10), int(4*hauteur/10)))
	zoneEdit.fill((238, 238, 238))
	
	#Flèche (premier appel)
	fleche = pygame.image.load("img/fleche.png").convert_alpha()
	fleche_rect = fleche.get_rect()
	
	#Boutons d'édition (premier appel)
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

	#on dessine la zone(premier appel)
	edition, niveau = resetZoneEdition(4)
	
	#Musique maestro !
	pygame.mixer.music.load("sons/editeur.mp3")
	pygame.mixer.music.play()
	
	pygame.display.flip()
	clock = pygame.time.Clock()
	
	#Boucle principale
	while running:
	
		largeur, hauteur = pygame.display.get_surface().get_size()
		
		#si la musique se termine, on la relance
		if pygame.mixer.music.get_busy()!=True:
    			pygame.mixer.music.play()
		
		for event in pygame.event.get():
		
			#fermeture de fenetre
			if event.type == pygame.QUIT:
				pygame.mixer.music.stop()
				running = False
			#gestion des evenements de la souris
			if pygame.mouse.get_focused():
				print str(niveau)
				x, y = pygame.mouse.get_pos()
				
				collide = fleche_rect.collidepoint(x, y)
		
				#bouton retour au menu
				if collide:
					pressed = pygame.mouse.get_pressed()
					if pressed[0]: 
						pygame.mixer.music.stop()
						running = False
				
				
				collide = terminer.collidepoint(x, y)
				
				#bout est termine?
				if collide:
					pressed = pygame.mouse.get_pressed()
					if pressed[0]: 
						if estRempli(niveau):
							liste = os.listdir('levels/')
							valide = False
							i = 0
							while(valide != True):
								nom = "CUSTOM" + str(i)
								valideux = True
								
								for c in range(len(liste)):
									if ((nom + ".lvl") == liste[c]):
										valideux = False
								
								if valideux:
									valide = True
								i += 1
								
							sauvegarde = Level(nom, 3*len(compteBloc), 4*len(compteBloc), 5*len(compteBloc))
							sauvegarde.setPosition(niveau)
							savelevel(sauvegarde)
							running = False
							
				
				
				collide = creation.collidepoint(x, y)
				
				#creationbloc
				if collide:
					pressed = pygame.mouse.get_pressed()
					if pressed[0]: 
						present = False
						for c in range(len(niveau)):
							for l in range(len(niveau[c])):
								if(niveau[c][l]==len(compteBloc)):
									present = True
						if present:
							compteBloc.append((r(), r(), r()))
							firstBloc = True
				
				
				collide = bloc4.collidepoint(x, y)
				
				#bouton choix 4*4
				if collide:
					pressed = pygame.mouse.get_pressed()
					if pressed[0]:
						zoneEdit.fill((238, 238, 238))
						compteBloc = [(r(),r(),r())]
						firstBloc = True
						screen.blit(zoneEdit, (1.25*largeur/10,  4*hauteur/10))
						edition, niveau = resetZoneEdition(4)
						
				collide = bloc5.collidepoint(x, y)	
					
				#bouton choix 5*5
				if collide:
					pressed = pygame.mouse.get_pressed()
					if pressed[0]:
						zoneEdit.fill((238, 238, 238))
						compteBloc = [(r(),r(),r())]
						firstBloc = True
						screen.blit(zoneEdit, (1.25*largeur/10,  4*hauteur/10))
						edition, niveau = resetZoneEdition(5)
				
				collide = bloc6.collidepoint(x, y)				
				#bouton choix 6*6
				if collide:
					pressed = pygame.mouse.get_pressed()
					if pressed[0]:
						zoneEdit.fill((238, 238, 238))
						compteBloc = [(r(),r(),r())]
						firstBloc = True
						screen.blit(zoneEdit, (1.25*largeur/10,  4*hauteur/10))
						edition, niveau = resetZoneEdition(6)
						
				#verification de la collision du tableau en entier		
				for c in range(len(edition)):
					for l in range(len(edition[c])):
						collide = edition[c][l].collidepoint(x, y)
						
						if collide:
							pressed = pygame.mouse.get_pressed()
							if pressed[0]:
								#on peut placer le premier bloc ou on veut
								if firstBloc:
									niveau[c][l] = len(compteBloc)
									firstBloc = False
								else:
									#un pixel du bloc se trouve-t-il a proximite ? Sinon,creation d'un nouveau bloc
									if verificationBloc(c, l, len(compteBloc)) and niveau[c][l] == 0:
										niveau[c][l] = len(compteBloc)
									else:
										if niveau[c][l] == 0:
											compteBloc.append((r(), r(), r()))
											niveau[c][l] = len(compteBloc)
						
				

		#ajout fleche				
		screen.blit(fleche, (0.10*largeur/10,  0.10*hauteur/10))
		pygame.font.init()
			
		#scene globale	
		editeur = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))
		
		#premiers textes	
		title_text("Place ton bloc ! - Creez votre niveau :", 1.25*largeur/10,  1.25*hauteur/10, (0, 0, 0), screen)
		normal_text("Bloc numero : ", 1.25*largeur/10,  1.25*hauteur/10 + 50, (0, 0, 0), screen)
		
		#nombre de blocs	
		zoneNbBlock = pygame.draw.rect(screen, (185,250,255), pygame.Rect(1.25*largeur/10 + 90, 1.25*hauteur/10+ 42, largeur/20, hauteur/20))
		nb = str(len(compteBloc))
		normal_text(nb, 1.25*largeur/10 + 101, 1.25*hauteur/10 + 52, (0, 0, 0), screen)
			
		creation = pygame.draw.rect(screen, [255,54,54], pygame.Rect(1.25*largeur/10 + 150, 1.25*hauteur/10 + 47, 70, 20))
		normal_text("Creer bloc", 1.25*largeur/10 + 158, 1.25*hauteur/10 + 52, (0, 0, 0), screen)
		
		#on redessine le tableau
		if(len(compteBloc)>=1 or firstBloc):
		
			zoneEdit.fill((238, 238, 238))
			screen.blit(zoneEdit, (1.25*largeur/10,  4*hauteur/10))
			edition = drawZoneEdition()
			
	
		bloc4 = pygame.draw.rect(screen, [185,250,255], pygame.Rect(1.25*largeur/10,  1.25*hauteur/10 + 90, 30, 15))
		normal_text("4*4", 1.25*largeur/10 + 5,  1.25*hauteur/10 + 91, (0, 0, 0), screen)
	
		bloc5 = pygame.draw.rect(screen, [185,250,255], pygame.Rect(1.25*largeur/10 + 35, 1.25*hauteur/10 + 90, 30, 15))
		normal_text("5*5", 1.25*largeur/10 + 40, 1.25*hauteur/10 + 91, (0, 0, 0), screen)
	
		bloc6 = pygame.draw.rect(screen, [185,250,255], pygame.Rect(1.25*largeur/10 + 70, 1.25*hauteur/10 + 90, 30, 15))
		normal_text("6*6",  1.25*largeur/10 + 75, 1.25*hauteur/10 + 91, (0, 0, 0), screen)
			
		terminer = pygame.draw.rect(screen, [255,54,54], pygame.Rect(int(8.75*largeur/10 - 90), 8.5*hauteur/10, 55, 16))
		normal_text("Terminer !", int(8.75*largeur/10 - 89), 8.5*hauteur/10 + 2, (0, 0, 0), screen)
		
		clock.tick(FPS)
		pygame.display.flip()
		
		pygame.font.quit()
			
	pygame.quit()
	
#le niveau est-il rempli de 1mini ?	
def estRempli(niveau):
    termine = True
    c = 0
    l = 0 
	
    while c < len(niveau) and termine != False:
    	while l < len(niveau[c]):
		if niveau[c][l] == 0:
			termine = False
		l+=1
	c+= 1
    return(termine)

#afficher du texte
def normal_text(texte, x, y, color, screen): 
    font_text = pygame.font.SysFont('roboto', 17)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))

#afficher du texte    
def title_text(texte, x, y, color, screen): 
    font_text = pygame.font.SysFont('roboto', 33)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))

#Reset ou definir pour la premier fois la zone de travail et le niveau
def resetZoneEdition(taille):
	
	largeur, hauteur = pygame.display.get_surface().get_size()
	
	edition = [[0]*taille for _ in range(taille)]
	niveau = [[0]*taille for _ in range(taille)] 
	a = (220, 220, 220)
	b = (230, 230, 230)
	
	
	for c in range(taille):
		i = 2+c
		for l in range(taille):
		
			if(i%2==0):
				edition[c][l] = pygame.draw.rect(screen , a, (int(1.25*largeur/10) +c*25, int(4*hauteur/10) + l*25, 25, 25))
			else:
				edition[c][l] = pygame.draw.rect(screen , b, (int(1.25*largeur/10) +c*25, int(4*hauteur/10) + l*25, 25, 25))
			i += 1
				
	return(edition, niveau)

#redraw	
def drawZoneEdition():
	
	largeur, hauteur = pygame.display.get_surface().get_size()
	
	a = (220, 220, 220)
	b = (230, 230, 230)

	
	for c in range(len(niveau)):
		i = 2+c
		for l in range(len(niveau[c])):
		
			if(i%2==0):
				if niveau[c][l] != 0:#(int(7.5*largeur/10), int(4*hauteur/10)) = zoneedit
					edition[c][l] = pygame.draw.rect(screen , compteBloc[niveau[c][l]-1], (int(1.25*largeur/10) +c*25, int(4*hauteur/10) + l*25, 25, 25))
					
				else:
					edition[c][l] = pygame.draw.rect(screen , a, (int(1.25*largeur/10) + c*25, int(4*hauteur/10) + l*25, 25, 25))
			else:
				if niveau[c][l] != 0:
					edition[c][l] = pygame.draw.rect(screen, compteBloc[niveau[c][l]-1], (int(1.25*largeur/10) + c*25, int(4*hauteur/10) + l*25, 25, 25))
					
				else:
					edition[c][l] = pygame.draw.rect(screen, b, (int(1.25*largeur/10) + c*25, int(4*hauteur/10) + l*25, 25, 25))
			i += 1
				
	return(edition)

#un pixel du bloc se trouve-t-il a proximite ?	
def verificationBloc(x, y, val):

	retour = True
	
	if x-1 < 0:#bord gauche ?
		if y-1<0:#bord bas ?
			if niveau[x+1][y] != val and niveau[x][y+1] != val :
				retour = False
		if y+1>=len(niveau[x]):#bord haut?
			if niveau[x][y-1] != val and niveau[x+1][y] != val:
				retour = False
		if y-1>=0 and y+1<len(niveau[x]):
			if niveau[x][y-1] != val and niveau[x+1][y] != val and niveau[x][y+1] != val:
				retour = False
	if x+1 >= len(niveau):#bord droit ?
		if y-1<0:#bord bas ?
			if niveau[x-1][y] != val and niveau[x][y+1] != val:
				retour = False
		if y+1>=len(niveau[x]):#bord haut ?
			if niveau[x][y-1] != val and niveau[x-1][y] != val:
				retour = False
		if y-1>=0 and y+1<len(niveau[x]) and niveau[x][y-1] != val and niveau[x-1][y] != val and niveau[x][y+1] != val:
			retour = False
					
	if x-1 >= 0 and x+1 < len(niveau):
		if y-1<0:#bord bas ?
			if niveau[x-1][y] != val and niveau[x][y+1] != val and niveau[x+1][y] != val:
				retour = False
		if y+1>=len(niveau[x]) and niveau[x][y-1] != val and niveau[x-1][y] != val and niveau[x+1][y] != val:#bord haut ?
			retour = False
			
		if y-1>=0 and y+1<len(niveau[x]) and niveau[x][y-1] != val and niveau[x-1][y] != val and niveau[x][y+1] != val and niveau[x+1][y] != val:
			retour = False
	
	return(retour)
