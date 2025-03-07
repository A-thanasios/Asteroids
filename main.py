import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    Shot.containers = (drawable, updatable, shots)

    player = Player(SCREEN_WIDTH / 2,
                    SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill((0, 0, 0))
        updatable.update(dt)
        for obj in asteroids:
            if obj.collide(player):
                print("Game Over!")
                sys.exit()

        for obj in asteroids:
            for shot in shots:
                if obj.collide(shot):
                    obj.get_hit()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()