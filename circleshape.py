import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Initialize the sprite first
        super().__init__()
        
        # Then add to containers if they exist
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
