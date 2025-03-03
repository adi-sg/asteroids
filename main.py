import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  #initialize the game and screen
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0 # delta time, amount of time since the last frame was drawn

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  asteroidfield = AsteroidField()

# game loop
  while(True):

    # check if the window is closed to terminate program
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill(color=(0,0,0))

    updatable.update(dt)

    for astr in asteroids:
      if astr.collision(player):
        print("Game Over!")
        return
      for shot in shots:
        if astr.collision(shot):
          astr.split()
          shot.kill()

    for draw_sprite in drawable:
      draw_sprite.draw(screen)
    
    pygame.display.flip()

    time = clock.tick(60)
    dt = time/1000

  # print("Starting asteroids!")
  # print(f"Screen width: {SCREEN_WIDTH}")
  # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
  main()