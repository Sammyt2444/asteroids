import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    
    def __init__(self, position, velocity):
        x = position.x
        y = position.y
        
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
        if self.__class__.containers:
            for container in self.__class__.containers:
                container.add(self)
        
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), 
                          (int(self.position.x), int(self.position.y)), 
                          self.radius)