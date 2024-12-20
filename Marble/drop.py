import pygame as pg
import constant as K
import math

class Drop:
    def __init__(self, r, center, color):
        self.r=r
        self.center=center
        self.color=color
        self.vertices=[self.center+self.r*P for P in K.UnitPoints]

    def isValid(self):
        return (self.center.x >0) and (self.center.x<K.SCREEN_WIDTH) and (self.center.y >0) and (self.center.y < K.SCREEN_HEIGHT)
    
    def update(self, prev_drop):
        # for d in drops:
        #     c = d.center
        #     self.vertices = [c+(p-c)*math.sqrt(1+self.r*self.r/(p-c).length_squared()) for p in self.vertices]
        
        c = prev_drop.center
        r = prev_drop.r
        self.vertices = [c+(p-c)*math.sqrt(1+r*r/(p-c).length_squared()) for p in self.vertices.copy()]

    def applytine(self, start, direction, normale, magnitude):
        
        u=1/pow(2,1/8)
        # u=0.5
        z=magnitude
        # d=(P-B).N
        # P = P+z*u^d*M
        for i in range(len(self.vertices)):
            p=self.vertices[i]
            d = abs((p-start).dot(normale))
            self.vertices[i]=p+z*pow(u, d)*direction



    def show(self, screen, debug=False):
        pg.draw.polygon(screen, self.color, self.vertices)
        if debug:
            for p in self.vertices:
                pg.draw.circle(screen, "white", p, 2)
        # pg.draw.lines(screen, self.color, False, self.vertices)
        # pg.draw.circle(screen, self.color, self.center, self.r, 1)
        # pg.draw.rect(screen, self.color, (self.center, (self.r, self.r)))