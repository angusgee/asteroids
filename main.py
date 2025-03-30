import pygame 
from constants import * 

import pygame

def main(): 
    pygame.init()
    pygame_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('>> exiting game...')
                return
        screen.fill('black')
        pygame.display.flip()
        time_passed = pygame_clock.tick(60)
        dt = time_passed / 1000
        print(dt)

if __name__ == "__main__":
    main()

