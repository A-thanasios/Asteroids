import random

import pygame.draw

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color=(255, 255, 255),
            center= self.position,
            radius = self.radius,
            width = 2
        )

    def get_hit(self):
        self.kill()

        if ASTEROID_MIN_RADIUS < self.radius:
            random_angle = random.uniform(20, 50)
            first_angle = self.velocity.rotate(random_angle)
            second_angle = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

            first_asteroid.velocity = first_angle * 1.2
            second_asteroid.velocity = second_angle * 1.2

