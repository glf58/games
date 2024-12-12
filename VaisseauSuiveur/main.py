import pygame as pg
from Vaisseau import Vaisseau
from suiveur import Suiveur
import constant as K


def main():

    pg.init()
    screen = pg.display.set_mode((K.SCREEN_WIDTH, K.SCREEN_HEIGHT))
    velocity = 1
    vaisseau = Vaisseau(position=pg.math.Vector2(10, 10), velocity=velocity)
    suiveur = Suiveur(position=pg.math.Vector2(600, 600),
                      color="red", velocity=1*velocity)
    clock = pg.time.Clock()
    running = True

    while running:

        screen.fill("black")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        vaisseau.update(target=pg.mouse.get_pos())
        vaisseau.draw(screen)
        suiveur.update(target=vaisseau.position)
        suiveur.draw(screen)
        pg.display.flip()

        dt = clock.tick(100) / 1000

    pg.quit()


if __name__ == "__main__":
    main()
