import pygame as pg
import constant as K


class Vaisseau:

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self, target):

        # direction=target-self.position
        # direction.normalize_ip()
        # self.position += self.velocity*K.dt*direction
        self.position.move_towards_ip(target, self.velocity * K.dt)

    def draw(self, screen):
        pg.draw.rect(surface=screen, color="blue",
                     rect=(self.position, (10, 10)))
