import pygame
from constants import *
from player import Player

def main():
  #initialize the game and screen
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0 # delta time, amount of time since the last frame was drawn

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)

  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  
# game loop
  while(True):

    # check if the window is closed to terminate program
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill(color=(0,0,0))

    updatable.update(dt)

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