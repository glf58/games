import pygame
import constant as K


class Vaisseau:
    def __init__(self, image):
        self.w, self.h = 50, 50
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.center = (K.GAME_WIDTH // 2  + K.top_left_x, K.BOTTOM - self.h//2)
        self.lives = 1
        self.vitesse = 1
        self.direction = 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # pygame.draw.rect(surface=surface, rect=self.rect, color="blue")
    
    def move(self):        
        self.rect = self.rect.move(self.direction*self.vitesse, 0)
        if (self.rect.bottomleft[0]<K.top_left_x) or (self.rect.bottomright[0]>K.top_left_x+K.GAME_WIDTH):
            self.rect = self.rect.move(-self.direction*self.vitesse, 0)      

