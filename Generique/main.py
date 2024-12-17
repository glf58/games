
import constant as K
import pygame as pg
import random
import colorsys
from MyClass import MyClass


def generate_random_color():

    # return "white"
    h, s, l = random.random(), 0.5 + random.random() / 2.0, 0.4 + random.random() / 5.0
    r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
    return (r, g, b)


def main():
    pg.init()
    screen = pg.display.set_mode((K.SCREEN_WIDTH, K.SCREEN_HEIGHT))
    running = True
    clock = pg.time.Clock()
    myclass = MyClass(5, pg.math.Vector2(100, 100), generate_random_color())
    while running:

        mouse_presses = pg.mouse.get_pressed()
        if mouse_presses[0]:
            print("Left Mouse Key is being pressed")

        # clock.tick(100) / 1000
        clock.tick(30)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill("black")
        myclass.update()
        myclass.show(screen)
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
