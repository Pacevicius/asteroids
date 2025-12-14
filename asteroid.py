from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
from random import uniform


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = uniform(20, 50)
        angle_split_1 = self.velocity.rotate(new_angle)
        angle_split_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_1.velocity = angle_split_1 * 1.2
        new_2.velocity = angle_split_2 * 1.2
