# -*- coding: iso-8859-15 -*-
import pygame
import os
from lecture import *
from save import *
from pygame.locals import *
from jeu import *
from editeur import *

#pseudo main du fichier
def menu():

    global LARGEUR, HAUTEUR
    LARGEUR, HAUTEUR = pygame.display.get_surface().get_size()
    running = True#le menu doit il continuer a fonctionner ? 
    FPS = 30
    retourdejeu = False#le menu s'affiche-t-il suite a un retour editeur ou de jeu ?
    
    #init + fond
    pygame.init() 
    screen = pygame.display.set_mode((640,480),HWSURFACE|DOUBLEBUF|RESIZABLE)
    pygame.display.set_caption("Place ton bloc ! - Menu")
    pygame.display.set_icon(pygame.image.load("img/icone.png")) 
    fond = pygame.image.load("img/background.jpg").convert()
    screen.blit(fond,(0,0))
    menu = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(LARGEUR/10,HAUTEUR/10, 8*LARGEUR/10, 8*HAUTEUR/10)) 
    pygame.mixer.music.load("sons/menu.mp3")
    pygame.mixer.music.play()
    pygame.display.flip()
    clock = pygame.time.Clock()
    

    #init du catalogue de niveaux
    niveau = []

    while running:
	
	#pseudo-traitement de l'exception : le menu revient avec pygame en off et il faut recreer la fenetre
	if retourdejeu:
		FPS = 30
   		pygame.init() 
    		screen = pygame.display.set_mode((640,480),HWSURFACE|DOUBLEBUF|RESIZABLE)
    
    		pygame.display.set_caption("Place ton bloc ! - Menu")
    		pygame.display.set_icon(pygame.image.load("img/icone.png"))
    
    		fond = pygame.image.load("img/background.jpg").convert()
    		screen.blit(fond,(0,0))
    		LARGEUR, HAUTEUR = pygame.display.get_surface().get_size()
    		menu = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(LARGEUR/10,HAUTEUR/10, 8*LARGEUR/10, 8*HAUTEUR/10))
    		pygame.mixer.music.load("sons/menu.mp3")
    		pygame.mixer.music.play()
    
   		pygame.display.flip()
    		clock = pygame.time.Clock()
   		 
    		running = True

    		niveau = []
    		retourdejeu = False
    		
    	if pygame.mixer.music.get_busy()!=True:
    		pygame.mixer.music.play()
    
        #possible resize
    	LARGEUR, HAUTEUR = pygame.display.get_surface().get_size()
    	
    	if LARGEUR > 400 or HAUTEUR > 400:   	
    		
    		#actualisation de la fenetre
		fond = pygame.image.load("img/background.jpg").convert()
    		screen.blit(fond,(0,0))
   		menu = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(LARGEUR/10,HAUTEUR/10, 8*LARGEUR/10, 8*HAUTEUR/10))
   		
    		pygame.font.init()
    		
    		#titre 1
    		title_text("Place ton bloc ! - Choisissez votre niveau :", LARGEUR/7,HAUTEUR/7, (0, 0, 0), screen)
    		normal_text("Niveaux standards :", LARGEUR/7,HAUTEUR/7 + 30, (0, 0, 0), screen)
    
    		#ajout dans le catalogue des niveaux des differents niveaux de base
    		try:
    			niveau.append(affichageniveau(lecture("baselevels/Niveau1.lvl"), LARGEUR/7, HAUTEUR/7 + 60, screen))
    			niveau.append(affichageniveau(lecture("baselevels/Niveau2.lvl"), LARGEUR/7, HAUTEUR/7 + 80, screen))
    			niveau.append(affichageniveau(lecture("baselevels/Niveau3.lvl"), LARGEUR/7, HAUTEUR/7 + 100, screen))
			niveau.append(affichageniveau(lecture("baselevels/Niveau4.lvl"), LARGEUR/7, HAUTEUR/7 + 120, screen))
			niveau.append(affichageniveau(lecture("baselevels/Niveau5.lvl"), LARGEUR/7, HAUTEUR/7 + 140, screen))
		except:
			print("Erreur : Un des niveaux de base est introuvable. Merci de verifier votre installation")
	
		#bouton pour acceder a l'editeur de niveaux
	
		edition = pygame.draw.rect(screen, [249,219,56], pygame.Rect(int(2*LARGEUR/3 -35), HAUTEUR/7 + 170, 30, 15))
		normal_text("Edit", int(2*LARGEUR/3 -31), HAUTEUR/7 + 171, (0, 0, 0), screen)
	
	
		try:
			#on recupere la liste des niveaux custom
    			liste = os.listdir('levels/')
			inter = 200

			#si il y a des niveaux custom, on les liste
			if liste:  
				#titre 2
    				normal_text("Niveaux custom :", LARGEUR/7,HAUTEUR/7 + 170, (0, 0, 0), screen)

    				for d in range(len(liste)):
    					if str(liste[d][len(liste[d])-4:len(liste[d])]) == ".lvl":	
    						niveau.append(affichageniveaucustom(lecture("levels/" + liste[d]), LARGEUR/7, HAUTEUR/7 + 200 + d*30, screen))
    		except:
    			print("Erreur : Impossible de lire les niveaux custom. Python a-t-il le droit de modifier des fichiers ?")
    			
    			
    		pygame.font.quit()
    		pygame.display.flip()
    
    		#gestion des evenements
    		for event in pygame.event.get():
    			#gestion fermeture fenetre
        		if event.type == pygame.QUIT:
				running = False
			#gestion du resize
      	 		elif event.type==VIDEORESIZE:
				screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
				screen.blit(pygame.transform.scale(fond,event.dict['size']),(0,0))
			#gestion des autres evenements si le menu ne fait pas directement suite a un retour, sinon erreur car pas de pygame.init
			if retourdejeu != True:
				#la souris est-elle sur la fenetre ?
   				if pygame.mouse.get_focused():
   			
        				x , y = pygame.mouse.get_pos()

       					c = 0
       					
       					#Est-elle sur le bouton edition ?
       					collide = edition.collidepoint(x, y)	
					if collide:
						#Click gauche ?
						try:
        						pressed = pygame.mouse.get_pressed()
        						if pressed[0]:
            							print "Editing ... "
            							pygame.mixer.music.stop()
								editeur()
								retourdejeu = True
						except:
							retourdejeu= True
							break
							
       					#verification de la position pour chaque bouton de niveau
       					while c < len(niveau):
       						if niveau[c][2] != 1:
							collide = niveau[c][2].collidepoint(x, y)
							if collide:
        						
        							pressed = pygame.mouse.get_pressed()
        							
        							if pressed[0]:				
									if os.path.isfile("levels/" + niveau[c][0].getNom() + ".lvl"):
										print "Deleting ... " + niveau[c][0].getNom()
										removesave(niveau[c][0])
   										os.remove("levels/" + niveau[c][0].getNom() + ".lvl")
    										niveau.remove(niveau[c])
    										pygame.time.wait(2000)
						c+=1
						
					#faire deux boucles n'est pas forcement optimal, mais permet de mieux separer les taches
					for c in range(len(niveau)):
						collide = niveau[c][1].collidepoint(x, y)

						if collide:
       							try:
        							pressed = pygame.mouse.get_pressed()
        							if pressed[0]:
            								print "Opening ... " + niveau[c][0].getNom()
            								pygame.mixer.music.stop()
									jeu(niveau[c][0])
									retourdejeu = True
							except:
								retourdejeu = True
								break
					

    	
    	else:#si la fenetre n'est pas en 400*400 mini...
    		pygame.font.init()
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

#Affichage d'un texte en Roboto taille 17 aux parametres x et y, de couleur choisie
def normal_text(texte, x, y, color, screen): 
    font_text = pygame.font.SysFont('roboto', 17)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))
    
#Affichage d'un texte en Roboto taille 33 aux parametres x et y, de couleur choisie    
def title_text(texte, x, y, color, screen): 
    font_text = pygame.font.SysFont('roboto', 33)
    affichage = font_text.render(texte, 1, (color))
    screen.blit(affichage,(x,y))
 
#Affiche le niveau de base passe en parametre. Affiche le nom du niveau et un bouton play interactif
def affichageniveau(niveau, x, y, screen):

    t, h = pygame.display.get_surface().get_size()
    
    normal_text(niveau.getNom(), x,y, (0, 0, 0), screen)
    
    panel = pygame.draw.rect(screen, [64,164,151], pygame.Rect(int(x+ 2*t/3), y, 30, 15))
    normal_text("Play", x + int(2*t/3 + 5), y, (0, 0, 0), screen)
    
    rang = pygame.image.load("img/" + str(lecturesave(niveau)) + ".png").convert_alpha()
    screen.blit(rang, (int(2*t/3 -30), y-5))
    
    retour = [niveau, panel, 1, 1]
    
    return(retour)
    
#Affiche le niveau custom passe en parametre. Affiche le nom du niveau, le rang via une image grace au fichier de sauvegarde et que deux boutons interactifs : un bouton play et un bouton delete
def affichageniveaucustom(niveau, x, y, screen):

    t, h = pygame.display.get_surface().get_size()
    
    normal_text(niveau.getNom(), x,y, (0, 0, 0), screen)
    
    suppr = pygame.draw.rect(screen, [255,0,0], pygame.Rect(int(x+ 2*t/3-10), y, 40, 15))
    normal_text("Delete", x + int(2*t/3 -5), y, (0, 0, 0), screen)
    
    play = pygame.draw.rect(screen, [64,164,151], pygame.Rect(int(x+ 2*t/3 - 40), y, 30, 15))
    normal_text("Play", x + int(2*t/3 + 5 - 40), y, (0, 0, 0), screen)
    
    rang = pygame.image.load("img/" + str(lecturesave(niveau)) + ".png").convert_alpha()
    screen.blit(rang, (int(2*t/3 -30), y-5))
    
    retour = [niveau, play, suppr]
    
    return(retour)
