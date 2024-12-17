import pygame as pg
import constant as K

class MyClass:
    def __init__(self, r, center, color):
        self.r=r
        self.center=center
        self.color=color

    def isValid(self):
        return (self.center.x >0) and (self.center.x<K.SCREEN_WIDTH) and (self.center.y >0) and (self.center.y < K.SCREEN_HEIGHT)
    
    def update(self):
        pass
        # self.center += pg.math.Vector2(1, 1)
        # if not self.isValid():
        #     self.center -= pg.math.Vector2(1, 1)

    def show(self, screen):
        pg.draw.rect(screen, self.color, (self.center, (self.r, self.r)))