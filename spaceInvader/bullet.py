import pygame
import constant as K


class Bullet:
    def __init__(self, x, y, is_enemy, speed):
        """ (x, y) est le coin superieur gauche """
        self.x = x
        self.y = y
        self.is_active = True
        self.is_enemy = is_enemy
        self.rect = pygame.Rect(self.x, self.y, K.BULLET_W, K.BULLET_H)
        self.speed = speed

    def draw(self, surface):
        if self.is_active:
            pygame.draw.rect(surface=surface, rect=self.rect, color="green" if self.is_enemy else "blue")

    def update(self):
        if self.is_enemy:
            if self.rect.bottom < self.speed + K.BOTTOM:
                self.rect = self.rect.move(0, self.speed)
            else:
                self.is_active=False
        else:
            if self.rect.top > self.speed + K.top_left_y:
                self.rect = self.rect.move(0, - self.speed)
            else:
                self.is_active = False
