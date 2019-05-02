# -*- coding: utf-8 -*-
 
import pygame
from pygame.locals import *
pygame.init()
fenetre=pygame.display.set_mode((460,480), RESIZABLE)
fond = pygame.image.load("Images/background.jpg")
fenetre.blit(fond, (0,0))
 
perso = pygame.image.load("Images/perso.png")
position_perso = fenetre.blit(perso, (0,0))
pygame.display.flip()
 
continuer=1
selected=0
 
while continuer:
    for event in pygame.event.get():
        if event.type ==  QUIT:
            continuer = 0
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and position_perso.collidepoint(event.pos):
            selected = 1
            print("selected")# cest la zone ou se trouve le personnage, si on clique dessus on considère quil est selectionné
 
        elif event.type == MOUSEBUTTONUP and event.button == 1 and selected:
            selected = 0
            print("unselected")#des quon lache le bouton de la souris, on considere que le personnage nest plus selectionne
             
        elif event.type == MOUSEMOTION and selected:
            r = fenetre.blit(fond, position_perso, position_perso)
            position_perso.move_ip(event.rel)#a chaque fois il y a mouvement de souris, le personnage prend la nouvelle position du curseur
            pygame.display.update((r,fenetre.blit(perso, position_perso)))
            print("move")
 
pygame.quit()