import pygame 
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main(): 
    pygame.init()
    pygame_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    # create groups
    updatable = set()
    drawable = set()
    
    # create asteroid group
    asteroids = pygame.sprite.Group()
    
    # set asteroid containers
    Asteroid.containers = asteroids, updatable, drawable

    # set asteroid field containers to a tuple
    AsteroidField.containers = (updatable,)

    # create asteroid field
    asteroid_field = AsteroidField()
    
    # Explicitly add to updatable to be sure
    updatable.add(asteroid_field)
    
    # create player in middle of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # add player to groups
    updatable.add(player)
    drawable.add(player)
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('>> exiting game...')
                return
        screen.fill('black')
        
        # update all updatable objects
        for obj in list(updatable):
            obj.update(dt)
        
        # Print debug info about asteroids
        print(f"Number of asteroids: {len(asteroids)}")
        
        # draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # render screen
        pygame.display.flip()

        # set to 60 FPS
        time_passed = pygame_clock.tick(60)
        dt = time_passed / 1000

if __name__ == "__main__":
    main()
