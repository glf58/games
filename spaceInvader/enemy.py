import pygame
import constant as K
from bullet import Bullet



class Enemy:
    def __init__(self, image):
        
        self.w, self.h = K.C, K.C
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.w, self.h))
        self.rect = self.image.get_rect()
        self.direction = 1
        self.is_active = True
        self.speed = 1
        self.can_shoot = False

    def draw(self, surface):
        if self.is_active:
            surface.blit(self.image, self.rect)

    def update(self, bullets):
        if self.is_active:
            self.rect = self.rect.move(self.direction*self.speed, 0)
            if (self.rect.right >= K.top_left_x+K.GAME_WIDTH) or (self.rect.left < K.top_left_x):
                self.rect = self.rect.move(-self.direction*self.speed, self.h)
                self.direction = -self.direction
            if (self.rect.bottom >= K.BOTTOM):
                self.is_active=False


