import pygame
from constants import *
from player import *

def main():
    pygame.init
    # setting screen variable and its dimensions for pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # While Loop
    running = True
    # FPS
    clock = pygame.time.Clock()
    dt = 0
    # Initialize player variable
    player = Player(x,y)
    
    # Game Logic
    while running:
        # This allows for the close button to work in the upper left hand corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fills screen variable with black color
        screen.fill(color=(0,0,0))
       
        # Player Triangle
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        player.draw(screen)

        # This allows for smooth screen refresh - allows for background and foreground data streams to swap - flicker gone
        pygame.display.flip()

        # pygame.time.Clock.tick(60)
        clock.tick(60)
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
