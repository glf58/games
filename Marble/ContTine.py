import constant as K
import pygame as pg
import random
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
    

def generate_background(nDrops, center, r):
    drops=[]
    for i in range(nDrops):
        addDrop(center, r, drops)
    return drops

def interpol(x, a, b, c, d):
    if x<=a:
        return c
    elif x >= b:
        return d  
    else:
        return (d-c)/(b-a)*(x-a)+c
         

def ContTine():
    pg.init()
    screen = pg.display.set_mode((K.SCREEN_WIDTH, K.SCREEN_HEIGHT))
    running = True
    clock = pg.time.Clock()
    drops=generate_background(100, K.CENTER, 50)
    screen.fill("black")
    for d in drops:
            d.show(screen)

    while running:

        # clock.tick(100) / 1000
        clock.tick(30)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # elif event.type == pg.KEYDOWN:
            #     if event.key == pg.K_SPACE:
            #         # print("Left Mouse Key is being pressed")
            #         drops.append( Drop(50+0*random.random(), pg.mouse.get_pos(), generate_random_color()))
            # elif event.type==pg.MOUSEBUTTONDOWN:
            #     start = pg.math.Vector2(pg.mouse.get_pos())
            #     print(start)
            # elif event.type==pg.MOUSEBUTTONUP:
            #     end = pg.math.Vector2(pg.mouse.get_pos())
            #     direction=end-start
            #     magnitude = interpol(direction.length(), 0, 600, 0, 50)
            #     direction.normalize_ip()
            #     normale = direction.rotate(90)
                
            #     screen.fill("black")                    
            #     for d in drops:
            #         d.applytine(start, direction, normale, magnitude)
            #         d.show(screen)
        
        
        mouse_presses = pg.mouse.get_pressed()      
        if mouse_presses[0]:
            start = pg.math.Vector2(pg.mouse.get_pos())
            direction = pg.math.Vector2(pg.mouse.get_rel())
            magnitude = direction.length()
            if magnitude >= 10:
                # print(magnitude)
                direction.normalize_ip()
                normale=direction.rotate(90)
                screen.fill("black")
                for d in drops:
                    d.applytine(start, direction, normale, 10)
                    d.show(screen)

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    ContTine()
