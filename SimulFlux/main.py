from math import tau
from champs import Champs
from ligne import lignedechamp
import constant as K
import pygame
import random
import colorsys


def generate_random_color():

    return "white"
    h, s, l = random.random(), 0.5 + random.random() / 2.0, 0.4 + random.random() / 5.0
    r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
    return (r, g, b)


def generate_random_position(centre):
    # X = random.randrange(K.XMIN, -K.XMIN)
    # Y = random.randrange(K.YMIN, -K.YMIN)
    # return pygame.math.Vector2(X,Y)
    Rmin = 100
    Rmax = 120
    V = pygame.math.Vector2()
    V.from_polar((Rmin + (Rmax - Rmin) * random.random(), 360 * random.random()))
    return V + centre


def main():
    pygame.init()
    screen = pygame.display.set_mode((K.SCREEN_WIDTH, K.SCREEN_HEIGHT))
    running = True
    racines = [
        complex(-200, -200),
        complex(200, 200),
        complex(-200, 200),
        complex(400, -200),
        # complex(1, 1),
    ]
    # racines = []
    racinesVect = [pygame.math.Vector2(r.real, r.imag) for r in racines]
    poles = [
        complex(-100.0, -100.1),
        complex(100.1, 100.1),
        complex(1.1, 1.1),
    ]
    # poles = []
    polesVect = [pygame.math.Vector2(p.real, p.imag) for p in poles]
    champs = Champs(poles=poles, racines=racines)
    clock = pygame.time.Clock()
    lignes = []
    NlignesdeChamp = 20
    tailledelaLigne = 100
    Vmin = 1 * K.C
    Vmax = 1 * K.C
    for i in range(NlignesdeChamp):
        lignes.append(
            lignedechamp(
                generate_random_position(random.choice(racinesVect + polesVect)),
                tailledelaLigne,
                generate_random_color(),
                # Vmin + (Vmax - Vmin) * random.random(),
                K.C,
                champs.grille,
            )
        )

    while running:

        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            # print("Left Mouse Key is being pressed")
            # x, y = event.pos
            x, y = pygame.mouse.get_pos()
            pos = pygame.math.Vector2(x - K.CENTER[0], y - K.CENTER[1])
            lignes.append(
                lignedechamp(pos, tailledelaLigne, "red", Vmin, champs.grille)
            )

        # clock.tick(100) / 1000
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # on genere la courbe issue du point ou l'utilisateur a clique
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     # x, y = pygame.mouse.get_pos()
            #     x, y = event.pos
            #     pos = pygame.math.Vector2(x - K.CENTER[0], y - K.CENTER[1])
            #     lignes.append(
            #         lignedechamp(pos, tailledelaLigne, "red", Vmin, champs.grille)
            #     )

        screen.fill("black")
        # champs.show(screen)
        for r in racines:
            pygame.draw.rect(
                screen, "red", rect=(r.real + K.CENTER[0], r.imag + K.CENTER[1], 3, 3)
            )
        for p in poles:
            pygame.draw.rect(
                screen, "green", rect=(p.real + K.CENTER[0], p.imag + K.CENTER[1], 5, 5)
            )

        for idx, l in enumerate(lignes):
            l.update(racinesVect)
            if l.respawn:
                lignes.pop(idx)
                lignes.append(
                    lignedechamp(
                        generate_random_position(
                            random.choice(racinesVect + polesVect)
                        ),
                        tailledelaLigne,
                        generate_random_color(),
                        # Vmin + (Vmax - Vmin) * random.random(),
                        K.C,
                        champs.grille,
                    )
                )
            l.draw(surface=screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
