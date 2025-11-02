import pygame
from constants import * 

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # setting screen dimensions for pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # While Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill(color=(0,0,0), rect=None, special_flags=0)
            pygame.display.flip()




if __name__ == "__main__":
    main()
