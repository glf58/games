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

# def generateSpiral(N, rayon, Rini):
    
#     drops = []
    
#     for i in range(N):
#         R = Rini+2*i*rayon
#         theta = 0
#         dtheta=2*math.asin(rayon/R)
#         while theta < K.TWOPI:
#             center = K.CENTER + R * pg.math.Vector2(math.cos(theta), math.sin(theta))
#             addDrop(center, rayon, drops)    
#             theta += dtheta
#     return drops

def getnewDrop(rayon, prevR, prevtheta):
    dtheta = 2*math.asin(rayon/prevR)
    theta = prevtheta + dtheta
    R = prevR
    if theta > K.TWOPI + 0.0001:
        R = prevR + 2*rayon
        dtheta = 2*math.asin(rayon/R)
        theta = 0   
    # center = K.CENTER+ R * pg.math.Vector2(math.cos(theta), math.sin(theta))
    # addDrop(center, rayon, drops)
    return (R, theta)

def PaintDropping():
    pg.init()
    screen = pg.display.set_mode((K.SCREEN_WIDTH, K.SCREEN_HEIGHT))
    running = True
    clock = pg.time.Clock()
    screen.fill("black")
    rayon=50
    prevR=rayon*math.sqrt(2)
    drops=[]
    Nsimul=100
    prevtheta=0
    while running:

        clock.tick(5)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        if (len(drops)<Nsimul):
            (R, theta) = getnewDrop(rayon, prevR, prevtheta)
            prevR = R
            prevtheta=theta
            center = K.CENTER+ R * pg.math.Vector2(math.cos(theta), math.sin(theta))
            addDrop(center, rayon, drops)
            screen.fill("black")
            for d in drops:
                d.show(screen)
                
            pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    PaintDropping()
