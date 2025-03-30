import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        if hasattr(Asteroid, 'containers'):
            self.containers = Asteroid.containers
            super().__init__(x, y, radius)
        else:
            super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', (int(self.position.x), int(self.position.y)), self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        # Manually remove from all containers before killing
        if hasattr(self, 'containers'):
            for container in self.containers:
                if self in container:
                    container.remove(self)
        
        # Kill the current asteroid (removes from pygame sprite groups)
        self.kill()
        
        # If the asteroid is too small, don't split it
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Generate a random angle between 20 and 50 degrees for splitting
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        
        # Scale up the velocities to make the smaller asteroids faster
        velocity1 *= 1.2
        velocity2 *= 1.2
        
        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
        
        # Add the new asteroids to the containers
        if hasattr(Asteroid, 'containers'):
            for container in Asteroid.containers:
                if asteroid1 not in container:
                    container.add(asteroid1)
                if asteroid2 not in container:
                    container.add(asteroid2)