import pygame

FPS = 30

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Place ton bloc ! - Menu")

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
