import pygame
from random import randint


class Balle:
    def __init__(self, image, center):
        self.image = pygame.image.load(image).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.vitesse = randint(1, 5)

    def affiche(self, fenetre):
        fenetre.blit(self.image, self.rect)

    def deplace(self):
        self.rect = self.rect.move(0, self.vitesse)

    def collision(self, targetRect):
        return self.rect.colliderect(targetRect)
