import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill() # every asteroid is always killed, and maybe we spawn more

    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      random_angle = random.uniform(20,50)
      v1 = self.velocity.rotate(random_angle)
      v2 = self.velocity.rotate(-1*random_angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS

      asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid1.velocity = v1 * random.uniform(1,1.3)
      asteroid2.velocity = v2 * random.uniform(1,1.3)

