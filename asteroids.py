from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color=(255,255,255), center=self.position, radius=self.radius, width=2)
    def update(self, dt):
        # forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.velocity * dt