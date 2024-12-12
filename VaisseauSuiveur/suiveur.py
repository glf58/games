import constant as K
import pygame as pg


class Suiveur:

    def __init__(self, position, velocity, color):
        self.position = position
        self.velocity = velocity
        self.color = color
        self.rect = pg.Rect((self.position, (5, 3)))

    def update(self, target):
        V = self.velocity*K.dt
        self.position.move_towards_ip(target, V)
        self.rect.center = self.position

    def draw(self, screen):
        pg.draw.rect(surface=screen, color=self.color, rect=self.rect)
