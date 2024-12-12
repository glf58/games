import constant as K

from vaisseau import Vaisseau
from bullet import Bullet
from enemy import Enemy
import pygame
from random import randint


def generate_grid(image, grid):
    for i in range(K.NROWS // 2):
        for j in range(K.NCOLS // 2):
            alien = Enemy(image)
            alien.rect.topleft = j * 2 * K.C + K.top_left_x, i * 2 * K.C + K.top_left_y

            if i == K.NROWS // 2 - 1:
                alien.can_shoot = True
            grid.append(alien)
    return grid


def check_alien_can_shoot(grid):
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((K.SCREEN_WIDTH, K.SCREEN_HEIGHT))
    running = True
    vaisseau = Vaisseau(
        "C://Users//papa//Documents//Python Scripts//games//spaceInvader//vaisseau.png"
    )
    bullets = []
    aliens = generate_grid(
        "C://Users//papa//Documents//Python Scripts//games//spaceInvader//alien.png", []
    )
    alienbullets = []

    clock = pygame.time.Clock()

    while running:

        clock.tick(100) / 1000
        screen.fill("black")
        pygame.draw.rect(
            surface=screen,
            rect=(K.TOP_LEFT, (K.GAME_WIDTH, K.GAME_HEIGHT)),
            color="red",
            width=1,
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # attention, avec cette syntaxe, on se retrouve avec une longue liste de bullets quans on appuie sur la touche d'espace
        if keys[pygame.K_RIGHT]:
            vaisseau.direction = 1
            vaisseau.move()
        if keys[pygame.K_LEFT]:
            vaisseau.direction = -1
            vaisseau.move()
        if keys[pygame.K_SPACE]:
            bullets.append(
                Bullet(
                    vaisseau.rect.centerx,
                    vaisseau.rect.top + K.BULLET_H // 2,
                    False,
                    speed=5,
                )
            )

        # update vaisseau's position
        vaisseau.draw(screen)
        screen.blit(vaisseau.image, vaisseau.rect)

        # update bullets
        for bullet in bullets:
            if bullet.is_active:
                bullet.update()
                bullet.draw(screen)
            else:
                bullets.remove(bullet)

        # update aliens' positions
        for alien in aliens:
            alien.update(bullets=bullets)
            alien.draw(screen)
            # check if alien is hit by bullet
            idx = alien.rect.collidelist([b.rect for b in bullets])
            if idx > 0:
                alien.is_active = False
                aliens.remove(alien)
                del bullets[idx]
            # alien is alive and can shoot
            if alien.can_shoot and randint(1, 1000) <= 0:
                alienbullets.append(
                    Bullet(
                        alien.rect.centerx,
                        alien.rect.bottom + K.BULLET_H // 2,
                        True,
                        speed=1,
                    )
                )
            # update aliens' bullets
        for b in alienbullets:
            if b.is_active:
                b.update()
                b.draw(screen)
                if b.rect.colliderect(vaisseau.rect):
                    b.is_active = False
                    vaisseau.lives -= 1
            else:
                alienbullets.remove(b)
        # update simulation
        pygame.display.update()
        # check end game
        if len(aliens) == 0:
            running = False
            print("Gagne")
        elif (vaisseau.lives <= 0) or (
            aliens[0].rect.bottom >= K.top_left_y + K.GAME_HEIGHT - vaisseau.h
        ):
            running = False
            print("Game Over")

    pygame.quit()


if __name__ == "__main__":
    main()
