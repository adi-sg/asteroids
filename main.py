import pygame
from constants import *

def main():
  #i nitialize the game and screen
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0 # delta time, amount of time since the last frame was drawn

# game loop
  while(True):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill(color=(0,0,0))
    
    pygame.display.flip()

    time = clock.tick(60)
    dt = time/1000

  # print("Starting asteroids!")
  # print(f"Screen width: {SCREEN_WIDTH}")
  # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
  main()