import pygame
from constants import * 

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # setting screen variable and its dimensions for pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # While Loop
    running = True
    
    # FPS
    clock = pygame.time.Clock()
    dt = 0
    
    while running:
        # This allows for the close button to work in the upper left hand corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fills screen variable with black color
        screen.fill(color=(0,0,0))
        # This allows for smooth screen refresh - allows for background and foreground data streams to swap - flicker gone
        pygame.display.flip()
        # pygame.time.Clock.tick(60)
        clock.tick(60)
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
