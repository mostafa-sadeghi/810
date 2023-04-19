import pygame

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
