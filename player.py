import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


PLAYER_SHOOT_COOLDOWN = 0.3

class Player(CircleShape):
    def __init__(self, x, y):
        # Initialize the parent class properly with all required parameters
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        
        # Player-specific properties
        self.rotation = 0
        
        self.cooldown_timer = 0
        
        
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            2
        )
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def update(self, dt):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt
        if self.cooldown_timer < 0:
            self.cooldown_timer = 0
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
            
            
    def shoot(self, shots_group):
        if self.cooldown_timer > 0:
            return
        
        shot_velocity = pygame.Vector2(0, 1)
        shot_velocity.rotate_ip(self.rotation)
        shot_velocity = shot_velocity * PLAYER_SHOOT_SPEED
        new_shot = Shot(pygame.Vector2(self.position), shot_velocity)
        if isinstance(shots_group, pygame.sprite.Group):
            shots_group.add(new_shot)
        else:
            shots_group.append(new_shot)
            
        self.cooldown_timer = PLAYER_SHOOT_COOLDOWN
            
            
    def handle_input(self, keys, shots_group):
        if keys[pygame.K_SPACE]:
            self.shoot(shots_group)


