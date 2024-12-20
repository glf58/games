import constant as K
import pygame as pg
import random, math
import colorsys
from drop import Drop


def generate_random_color():

    # return "white"
    h, s, l = random.random(), 0.5 + random.random() / 2.0, 0.4 + random.random() / 5.0
    r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
    return (r, g, b)

def addDrop(center, r, drops):
    newDrop=Drop(r, center, generate_random_color())
    for d in drops:
        d.update(newDrop)
    drops.append(newDrop)

def SingleDropPainting():
    pg.init()
    screen = pg.display.set_mode((K.SCREEN_WIDTH, K.SCREEN_HEIGHT))
    running = True
    clock = pg.time.Clock()
    screen.fill("black")
    rayon=50
    drops=[]

    while running:

        clock.tick(20)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONUP:
                center = pg.math.Vector2(pg.mouse.get_pos())
                addDrop(center, rayon, drops)
                screen.fill("black")
                for d in drops:
                    d.show(screen)
            
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    SingleDropPainting()
