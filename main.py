import pygame
from constants import *
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()  
    drawable = pygame.sprite.Group()   
    asteroids = pygame.sprite.Group()  
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable) 
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        keys = pygame.key.get_pressed()
        player.handle_input(keys, shots)
        
        dt = clock.tick(60) / 1000 
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                dx = asteroid.position.x - shot.position.x
                dy = asteroid.position.y - shot.position.y
                distance = (dx**2 + dy**2)**0.5
                if distance < (asteroid.radius + shot.radius):
                    asteroid.split()
                    shot.kill()
        
        screen.fill("black")
        
        for drawable_object in drawable:
            drawable_object.draw(screen)
        
        pygame.display.flip()

        # print("Starting Asteroids!")  
        # print(f"Screen width: {SCREEN_WIDTH}")
        # print(f"Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()
