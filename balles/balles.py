import pygame
from pygame import display
from pygame.locals import *
from balle import Balle
from random import randint

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load(
    "C:/Users/papa/Documents/Python Scripts/games/balles/fond.png"
).convert()
blob = pygame.image.load(
    "C:/Users/papa/Documents/Python Scripts/games/balles/blob2.png"
).convert_alpha()
blob.set_colorkey((255, 255, 255))
blobRect = blob.get_rect()
blobRect.topleft = (270, 380)
fenetre.blit(fond, (0, 0))

cont = True
listeBalles = []

while cont:
    if len(listeBalles) < 10 and randint(1, 500) <= 10:
        listeBalles.append(
            Balle(
                "C:/Users/papa/Documents/Python Scripts/games/balles/balle.png",
                (randint(25, 455), -25),
            )
        )
    for event in pygame.event.get():
        if event == QUIT:
            cont = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                blobRect = blobRect.move(-10, 0)
            if event.key == K_RIGHT:
                blobRect = blobRect.move(10, 0)

    fenetre.blit(fond, (0, 0))
    for balle in listeBalles:
        balle.deplace()
        if balle.rect.top >= 480:
            listeBalles.remove(balle)
        else:
            if balle.collision(blobRect):
                cont = False
            balle.affiche(fenetre)

    fenetre.blit(blob, blobRect)
    pygame.display.update()
    pygame.time.wait(10)

pygame.quit()
