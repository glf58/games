import pygame
import constant as K
import cmath, math


class Champs:
    def __init__(self, poles, racines):
        self.poles = poles
        self.racines = racines
        self.grille = []
        self.genereGrille()

    # on normalise les vitesses pour ne considerer que la direction donnee par le champs. L'effet de vitesse est ajoute au niveau du calcul de la ligne de champs
    # ceci permet de simuler des champs avec des intensites tres differentes, comme ce que l'on observe en melangeant des poles et des racines

    def flux(self, X, Y):
        z = complex(X, Y)
        res = 1
        for r in self.racines:
            res = res * (z - r)
        for p in self.poles:
            res = res / (z - p)
        return (
            pygame.math.Vector2(0, 0)
            if abs(res) == 0
            else pygame.math.Vector2(res.real, res.imag).normalize()
        )

    def genereGrille(self):
        for i in range(K.NLIGNES):
            Y = K.YMIN + i * K.C
            for j in range(K.NCOLS):
                X = K.XMIN + j * K.C
                V = self.flux(X, Y)
                self.grille.append(V)

    def show(self, surface, maxVectorSize=30):
        for i in range(K.NLIGNES):
            Y = K.YMIN + i * K.C
            for j in range(K.NCOLS):
                X = K.XMIN + j * K.C
                start = pygame.math.Vector2(X, Y) + K.CENTER
                pygame.draw.line(
                    surface=surface,
                    color="blue",
                    start_pos=start,
                    end_pos=start + self.grille[j + i * K.NCOLS] * maxVectorSize,
                )
