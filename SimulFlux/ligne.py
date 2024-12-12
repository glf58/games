import pygame
import math
import constant as K


class lignedechamp:
    def __init__(self, currentpoint, taille, couleur, v, grille):
        self.currentpoint = currentpoint
        self.points = [self.currentpoint]
        self.taille = taille
        self.couleur = couleur
        self.v = v
        self.grille = grille
        self.respawn = False

    def aConverge(self, racines):
        d = 1e9
        for r in racines:
            d = min((self.currentpoint - r).length(), d)
        return d < K.C

    def update(self, racines):
        if len(self.points) > 0:
            i = math.floor((self.currentpoint[1] - K.YMIN) / K.C)
            j = math.floor((self.currentpoint[0] - K.XMIN) / K.C)
            idx = j + i * K.NCOLS

            V = self.v * self.grille[idx]
            self.currentpoint = self.points[-1] + V
            if (
                (abs(self.currentpoint[0]) <= -K.XMIN)
                and (abs(self.currentpoint[1]) <= -K.YMIN)
                # and (V.length() > 0.001)
                and not self.aConverge((racines))
            ):
                self.points.append(self.currentpoint)
            else:
                self.currentpoint = self.points[-1]
                self.points.pop(0)
            if len(self.points) >= self.taille:
                self.points.pop(0)
        else:
            self.respawn = True

    def draw(self, surface):
        if len(self.points) > 1:
            pygame.draw.lines(
                surface=surface,
                color=self.couleur,
                closed=False,
                points=[p + K.CENTER for p in self.points],
                width=1,
            )
