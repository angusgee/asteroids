import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        
        if hasattr(self, 'containers'):
            for container in self.containers:
                if self not in container:
                    container.add(self)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_collisions(self, other):
        # Calculate distance between the centers of the two shapes
        distance = self.position.distance_to(other.position)
        
        # Check if the distance is less than or equal to the sum of the radii
        return distance <= (self.radius + other.radius)
