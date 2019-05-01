import pygame
from pygame.locals import *
from math import sin
import time

FPS = 30

pygame.init()
fenetre = pygame.display.set_mode((640, 480), HWSURFACE|DOUBLEBUF|RESIZABLE)
fond = pygame.image.load("Images/background.jpg").convert()
fenetre.blit(fond, (0,0))

logo = pygame.image.load("Images/URCA.png").convert_alpha()

pygame.mixer.music.load("Sons/intro.mp3")

pygame.display.flip()
clock = pygame.time.Clock()  
	
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type==VIDEORESIZE:
			screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
			screen.blit(pygame.transform.scale(fond,event.dict['size']),(0,0))
			largeur, hauteur = pygame.display.get_surface().get_size()
			fenetre.blit(logo, ((largeur/2) - 50, hauteur*0.8))
			pygame.mixer.music.play()
		
	clock.tick(FPS)
	pygame.display.flip()
	

pygame.mixer.music.stop()
pygame.quit()