import pygame 
from constants import * 
from player import Player

def main(): 
    pygame.init()
    pygame_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    # Create player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('>> exiting game...')
                return
        screen.fill('black')
        player.draw(screen)
        pygame.display.flip()
        time_passed = pygame_clock.tick(60)
        dt = time_passed / 1000

if __name__ == "__main__":
    main()
