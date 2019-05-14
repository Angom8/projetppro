#La ou toute la magie opere !
# -*- coding: iso-8859-15 -*-
import pygame
import os
from lecture import *
from pygame.locals import *
from save import *
import random
import time

#Fonction principale
def jeu(niveau):

    FPS = 30
    pygame.init()
    pygame.font.init()
    
    global ecran#la fenetre global
    global zoneblocs, zonejeu#zoneblocs = premier rectangle gris en haut, zonejeu = le deuxieme
    
    running = True
    gameover = False#Le joueur a-t-il perdu ?
    enjeu= False#le joueur a-t-il lance la partie ?
    bloc_grab = False#un bloc est-il en cours de grab ?
    
    ecran = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Place ton bloc ! - " + niveau.getNom())
    pygame.display.set_icon(pygame.image.load("img/icone.png"))
    fond = pygame.image.load("img/background.jpg").convert()
    ecran.blit(fond,(0,0))
    largeur, hauteur = pygame.display.get_surface().get_size()
    
	
    zoneblocs = pygame.Surface((int(7.5*largeur/10), int(2.5*hauteur/10))) 
    pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))
    pygame.display.flip()
    
    #init timer
    clock = pygame.time.Clock()
    counter, text = 180, '180'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    #la zone blanche globale derrier les deux autres
    zglobal = pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))

    #on imprime la zone des blocs, ainsi que ces derniers dans celle-ci
    zoneblocs = pygame.Surface((int(7.5*largeur/10), int(2.5*hauteur/10)))	
    zoneblocs.fill((245, 245, 245))
    blocs = drawBlocs(14*largeur/10, 1.25*hauteur/10, niveau)#blocs contient des blocs avec leurs "pixels" possedant leur rect ainsi que leur couleur, le tout est un assemblage de tableaux
    ecran.blit(zoneblocs, (1.25*largeur/10,  1.25*hauteur/10))
    	
    #on imprime la zone de jeu
    zonejeu = pygame.Surface((int(7.5*largeur/10), int(4*hauteur/10)))
    zonejeu.fill((245, 245, 245))
    ecran.blit(zonejeu, (1.25*largeur/10,  4*hauteur/10))
   
    #on imprime le bouton terminer
    termine = pygame.draw.rect(ecran, [64,164,151], pygame.Rect(int(8.75*largeur/10 - 48), 8.5*hauteur/10, 48, 15))
    normal_text("Terminer", int(8.75*largeur/10 - 49), 8.5*hauteur/10, (0, 0, 0), ecran)	

    #ainsi que le bouton play
    play = pygame.draw.rect(ecran, [64,164,151], pygame.Rect(int(8.75*largeur/10 - 90), 8.5*hauteur/10, 30, 15))
    normal_text("Play", int(8.75*largeur/10 + 5 - 90), 8.5*hauteur/10, (0, 0, 0), ecran)
    
    #on initialise le tableau de verification (toutes les cases doivent etre pleines, avec des 1)
    tab = [[0] * len(niveau.getPosition()[0]) for _ in range(len(niveau.getPosition()))]
    
    while running:
    	font = pygame.font.SysFont('Consolas', 20)
    	for event in pygame.event.get():
    		#une fermeture de fenetre renvoie sur menu par le biais des try/catch
    		if event.type == pygame.QUIT:
    			running = False
    		#decompte du timer s'il est en cours
		if event.type == pygame.USEREVENT and enjeu == True: 
            			counter -= 1
           			if counter < 0:
           				gameover = True		
           			else:
           				text = str(counter).rjust(3)
           				
           				
           	#evenements de la souris
		if pygame.mouse.get_focused():
        			x , y = pygame.mouse.get_pos()

				#collide pour le bouton Play, qui commence le jeu
				collide = play.collidepoint(x, y)
				if collide:
        				pressed = pygame.mouse.get_pressed()
        				if pressed[0]:
        					jeuencours = drawzonejeu(niveau)
            					enjeu = True
            					
            			#collide pour le bouton Terminer, qui arrete tout et renvoie sur le menu en imprimant le score s'il est bon (via estTermine)		
            			collide = termine.collidepoint(x, y)
				if collide:
        				pressed = pygame.mouse.get_pressed()
        				if pressed[0]:
            					if estTermine:
            						if (counter + niveau.getRang(3)) < 180:            						
            							addsave(niveau, 3)
            						elif (counter + niveau.getRang(2)) < 180:
            							addsave(niveau, 2)
            						elif (counter + niveau.getRang(1)) < 180:
            							addsave(niveau, 1)
            						enjeu = False
            						running = False
            						
            			#GRAB : Si on relache la souris, le grab se finit. On se demande alors si le bloc est bien dans le tableau de la zone de jeu et s'il empiete sur un autre bloc 			
				if event.type == MOUSEBUTTONUP and bloc_grab and enjeu:
					bloc_grab = False
					
					if verif_superpositionbloc(blocs, bloc_move):
						placement = verif_superpositionzonejeu(jeuencours, bloc_move)
						if placement[0]:
							for p in range(len(placement[1])):
								g, h = conversion_tab(tab, placement[1][p])
								tab[g][h] = 1
					bloc_move = None
				
				#GRAB : C'est assez complexe
				if event.type == MOUSEBUTTONDOWN and enjeu :
					if event.button == 1:
						c = 0
						l = 0
						d = 0
						verif = False
						
						#premierement, on detecte la presence d'un bloc sous le clic
						while c < len(blocs) and verif == False:
							while l < len(blocs[c]) and verif == False:
								x, y = event.pos
								if blocs[c][l][0].collidepoint(x, y):#le pixel du bloc c dans le tableau blocs est-il en contact avec la souris ?
									bloc_grab = True#on active le grapin
									bloc_move = blocs[c]#le bloc grab est save
									
									#on le retire du tableau de zonedejeuu s'il y etait et n'etait pas superpose a un autre bloc						
									if verif_superpositionbloc(blocs, bloc_move):
										placement = verif_superpositionzonejeu(jeuencours, bloc_move)
										if placement[0]:
											for p in range(len(placement[1])):
												g, h = conversion_tab(tab, placement[1][p])
												tab[g][h] = 0
									verif = True#on sort de la boucle
                   						l += 1
                   					l = 0
							c += 1
				#GRAB : Ensuite, on deplace le bloc. Grosse difficulte : Il faut aussi deplacer tous les pixels !
				elif event.type == pygame.MOUSEMOTION and enjeu:
					x, y = event.pos
					a = x
					b = y
         				if bloc_grab:
         					d = 0
						for d in range(len(bloc_move)):#Pour chaque pixel du bloc en cours
							if d == 0:#C'est le premier pixel. Peut causer un decalage sur les gros blcos
								xprec = bloc_move[d][0].x#On sauvegarde l'ancienne position
								yprec = bloc_move[d][0].y
								bloc_move[d][0].x = x#On definit la position du bloc 0 a celle de la souris
								bloc_move[d][0].y = y
							else:
								if bloc_move[d][0].x>xprec and bloc_move[d][0].y==yprec:#si le deuxieme pixel est sur la meme ligne que le precedent
									xprec = bloc_move[d][0].x#on sauvegarde l'ancienne position
									yprec = bloc_move[d][0].y
									a += 25#on ajoute l'espace reglementaire entre deux pixels
									bloc_move[d][0].x = a#on definit la position du bloc n a celle de la sours + ecart par rapport au bloc 0
									bloc_move[d][0].y = b
								elif bloc_move[d][0].y>yprec:#si nouvelle ligne, probleme : comment determiner si le bloc est en recul par rapport aux autres de la ligne d'avant ?
									while bloc_move[d][0].x<xprec:#Solution : Tq on a un decalage entre l'ancienne position du bloc n-1 et la position actuelle avant deplacement du bloc n, on retire l'espace pour decaler la position
											a-=25
											xprec -=25
									xprec = bloc_move[d][0].x
									yprec = bloc_move[d][0].y
									b += 25#nouvelle ligne, donc ecart
									bloc_move[d][0].x = a
									bloc_move[d][0].y = b
	
	largeur, hauteur = pygame.display.get_surface().get_size()
	
	#on actualise globalement la fenetre pour eviter de voir se dessiner des petits blocs un peu partout lors du grab !
	fond = pygame.image.load("img/background.jpg").convert()
    	ecran.blit(fond,(0,0))
	zglobal = pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(largeur/10,hauteur/10, 8*largeur/10, 8*hauteur/10))								
  	
  	ecran.blit(zoneblocs, (1.25*largeur/10,  1.25*hauteur/10))
    	
        zonejeu = pygame.Surface((int(7.5*largeur/10), int(4*hauteur/10)))
        zonejeu.fill((245, 245, 245))
        ecran.blit(zonejeu, (1.25*largeur/10,  4*hauteur/10))
        
        #si on est en jeu, on place un tableau a remplir
        if enjeu == True:
   		jeuencours = drawzonejeu(niveau)
   		drawaffichagejeu(niveau, tab)
   		#petite aide
   		ecran.blit(font.render("Les blocs ne doivent pas se toucher !", True, (0, 0, 0)), (4*largeur/10, 7.5*hauteur/10))
   		
   	#on redessine les differents blocs
   	reDraw(blocs)
   	
   	#on imprime de nouveau les boutons pour eviter d'avoir des blocs dessus
        termine = pygame.draw.rect(ecran, [64,164,151], pygame.Rect(int(8.75*largeur/10 - 48), 8.5*hauteur/10, 48, 15))
        normal_text("Terminer", int(8.75*largeur/10 - 49), 8.5*hauteur/10, (0, 0, 0), ecran)
        play = pygame.draw.rect(ecran, [64,164,151], pygame.Rect(int(8.75*largeur/10 - 90), 8.5*hauteur/10, 30, 15))
        normal_text("Play", int(8.75*largeur/10 + 5 - 90), 8.5*hauteur/10, (0, 0, 0), ecran)
        
	#on fait pareil avec le timer
	fondtimer = pygame.Surface((int(0.5*largeur/10), int(0.5*hauteur/10)))
  	fondtimer.fill((255,255,255))
  	ecran.blit(fondtimer, (1.25*largeur/10,  8.5*hauteur/10))
   	ecran.blit(font.render(text, True, (0, 0, 0)), (1.25*largeur/10, 8.5*hauteur/10))
   	

        clock.tick(FPS)
        #ne pas supprimer font sature le processus
        
        if gameover == True:
   		ecran.blit(font.render("Game over ! Retour au menu ...", True, (255, 0, 0)), (3*largeur/10, 8.5*hauteur/10))
   		pygame.display.flip()
   		pygame.time.wait(4000)
   		running = False
   	del font
        pygame.display.flip()
    pygame.font.quit() 
    pygame.quit()
   
#Redessiner les blocs a leurs nouvelles positions
def reDraw(blocs):    
    
    for c in range(len(blocs)):
    	for l in range(len(blocs[c])):
    		pygame.draw.rect(ecran , blocs[c][l][1],  blocs[c][l][0])

#Permet d'obtenir un tableau contenant lui-meme le tableau de chaque bloc avec ses positions    
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

#transforme les positions de l'objet niveau en tableau de position pour un bloc
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

#On dessine le bloc, valable pour la premier apparition    		
def drawBloc(x, y, leBloc):

    r = lambda: random.randint(0,255)#obtention d'une couleur aleatoire et unique pour tout le bloc
    largeur, hauteur = pygame.display.get_surface().get_size()
    zebloc = []
    a = (r(),r(),r())
    for l in range(len(leBloc)):
        for c in range(len(leBloc[0])):
        	if leBloc[l][c] != 0:
        		pixel = pygame.draw.rect(ecran , a, (1.25*largeur/10+x+ (c*25), 1.25*largeur/10+y+(l*25), 25, 25))
        		zebloc.append([pixel, a])
    return zebloc  
      		
#Fonction pour dessiner tous les blocs
def drawBlocs(u, v, niveau):

    t = (v)
    blocs = creerBlocs(niveau)
    retour = []
    t = t/(len(blocs))
    c = 0
    x = t
    y = t
    random.shuffle(blocs)#on remue le tableau pour ne pas afficher la solution !
    for c in range(len(blocs)):
    	
    	if(x>u):
    		y += t
    		
    	retour.append(drawBloc(x, y, blocs[c]))
    	x +=  t
    	
    return(retour)

#Fonction pour dessiner la zone de jeu (le tableau de reponse). Retourne un tableau avec les differents RECT de chaque case, vu que l'element est graphique    
def drawzonejeu(niveau):


    largeur, hauteur = pygame.display.get_surface().get_size()
    	
    jeuencours = []
    a = (220, 220, 220)
    b = (230, 230, 230)
    
    
    for c in range(len(niveau.getPosition())):
    	i = 2+c
    	for l in range(len(niveau.getPosition())):
    	
    		if(i%2!=0):
   			jeuencours.append(pygame.draw.rect(ecran , a, (1.25*largeur/10+c*27, 4*largeur/10+l*27, 27, 27)))
   		else:
   			jeuencours.append(pygame.draw.rect(ecran , b, (1.25*largeur/10+c*27, 4*largeur/10+l*27, 27,27)))
   		i+=1
   			
    return(jeuencours)
    
#Fonction pour dessiner l'affichage zone de jeu.  
def drawaffichagejeu(niveau, tab):


    largeur, hauteur = pygame.display.get_surface().get_size()
    	
    a = (220, 220, 220)
    b = (93, 218, 49)
    
    for c in range(len(niveau.getPosition())):
    
    	for l in range(len(niveau.getPosition())):
    	
    		if(tab[l][c]==0):
   			pygame.draw.rect(ecran , a, (1.25*largeur/10+c*27 +200, 4*largeur/10+l*27, 27, 27))
   		else:
   			pygame.draw.rect(ecran , b, (1.25*largeur/10+c*27 +200, 4*largeur/10+l*27, 27,27))

#Le jeu se termine quand toutes les cases sont pleines, peu import s'il s'agissait vraiment du bon bloc. Il n'existe ainsi pas qu'une seule solution pour un niveau !
def estTermine(tab, niveau):
	i = 0
	j = 0
	verif = True
	
	while i < len(tab) and verif == True:
		while j < len(tab[i]):
			if tab[i][j] != 0:
				verif = False
			j += 1
		j +=1
	
	return verif
	
#Affichage d'un texte en Roboto taille 17 aux parametres x et y, de couleur choisie	
def normal_text(texte, x, y, color, ecran): 
    font_text = pygame.font.SysFont('roboto', 17)
    affichage = font_text.render(texte, 1, (color))
    ecran.blit(affichage,(x,y))
    
#Affichage d'un texte en Roboto taille 33 aux parametres x et y, de couleur choisie     
def title_text(texte, x, y, color, ecran): 
    font_text = pygame.font.SysFont('roboto', 35)
    affichage = font_text.render(texte, 1, (color))
    ecran.blit(affichage,(x,y))
    
#Le bloc a-t-il un de ses pixels en superposition avec un autre bloc ?
def verif_superpositionbloc(blocs, lebloc):

    verif = True#collision avec un autre bloc ?
    z = 0
    p = 0
    u = 0
    while verif == True and  z < len(blocs):#parcours du tableau des blocs

	while verif == True and p < len(lebloc):#parcours des pixels du bloc
	
		while verif == True and u < len(blocs[z]):#parcours des pixels du deuxieme bloc
		
			if lebloc != blocs[z] and lebloc[p][0].colliderect(blocs[z][u][0]): #le pixel a -t-il une collision ?
				verif = False#oui donc on arrete tout
			
			u +=1
				
				
		u = 0
		p +=1
	p = 0
	z +=1

    return(verif)#si true : pas de superposition, si false : superposition donc pas de changement pour le tableau de sol

#tous les pixels du bloc sont-ils dans la zonedejeu ?    
def verif_superpositionzonejeu(jeuencours, lebloc):

	pospixels = []#tableau des positions, pratique pour plus tard
	p = 0
	verifun = True#un seul des pixels est-il en dehors de la zone
	
	while verifun == True and  p < len(lebloc):#parcours des differents pixels du bloc
	
		verifdeux = False#le pixel est-il dans une case ? Si oui, pospixels.append[c], sinon on arrete tout
		c = 0
		
		while verifun == True and c < len(jeuencours) and verifdeux == False:#parcours du tableau de solutions
			if lebloc[p][0].colliderect(jeuencours[c]) : 
				verifdeux = True
				pospixels.append(c)
				
			c += 1
				
		if verifdeux == False : 
			verifun = False#un des pixels n'est pas dans le tableau
		p+=1
		
	return([verifun, pospixels])#on retourne si oui ou non tous les pixels sont dans le coup et la position dans le tableau de ces derniers
	
def conversion_tab(tab, i):

	y = 0
	while i >= len(tab):
		i -= len(tab)
		y += 1
	x = i
	
	return(x, y)		
