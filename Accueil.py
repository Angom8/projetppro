import pygame
from pygame.locals import *
from math import sin
import time

FPS = 30

pygame.init()
fenetre = pygame.display.set_mode((640, 480), HWSURFACE|DOUBLEBUF|RESIZABLE)
fond = pygame.image.load("Images/background.jpg").convert()
fenetre.blit(fond, (0,0))

pygame.display.set_caption("Démarrage")

logo = pygame.image.load("Images/URCA.png").convert_alpha()

texte = "THEBAULT Antoine / ALEXANDRE Clément"
font = pygame.font.SysFont('Consolas', 20)

pygame.mixer.music.load("Sons/intro.mp3")

counter, text = 8, '180'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

pygame.display.flip()
clock = pygame.time.Clock()  
	
running = True

while running:
	pygame.init()	
	for event in pygame.event.get():
		if event.type == pygame.USEREVENT: 
			counter -= 1
			text = str(counter).rjust(3) if counter > 0 else pygame.quit()
		if event.type == pygame.QUIT:
			running = False
		elif event.type==VIDEORESIZE:
			screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
			screen.blit(pygame.transform.scale(fond,event.dict['size']),(0,0))
			largeur, hauteur = pygame.display.get_surface().get_size()
			pygame.mixer.music.play()
			fenetre.blit(logo, ((largeur/2) - 65, hauteur*0.45))
			pygame.display.flip()
			pygame.time.wait(4000)
			fenetre.blit(fond , (0,0))
			fenetre.blit(font.render(texte, True, (0, 0, 0)), ((largeur/5) , hauteur*0.5))
			pygame.display.flip()
			pygame.time.wait(3000)
			
			clock.tick(FPS)
	

pygame.mixer.music.stop()
pygame.quit()