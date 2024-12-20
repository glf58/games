import pygame as pg
import math

TWOPI = 2*3.1415926

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
CENTER=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
CircleRes = 50
Thetas = [TWOPI*k/CircleRes for k in range(CircleRes+1)]
UnitPoints = [pg.math.Vector2(math.cos(t), math.sin(t))for t in Thetas]