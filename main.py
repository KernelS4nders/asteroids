import sys
import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import * 

def main():
    pygame.init
    # setting screen variable and its dimensions for pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # While Loop initializer
    running = True
    # FPS and delta time initialization
    clock = pygame.time.Clock()
    dt = 0
    
    # Initialize player variable
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatable, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Initialize Asteroids Variable
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawables)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # shots
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawables)


    # Game Logic
    while running:
        # This allows for the close button to work in the upper left hand corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        # asteriod collision check
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()
                

        
        # Fills screen variable with black color
        screen.fill(color=(0,0,0))
        # Player Triangle
        
        for drawable in drawables:
            drawable.draw(screen)
        # player.draw(screen)
        # player.update(dt)
        # This allows for smooth screen refresh - allows for background and foreground data streams to swap - flicker gone
        pygame.display.flip()

        # pygame.time.Clock.tick(60)
        clock.tick(60)
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
