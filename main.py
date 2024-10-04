import pygame
from constants import *


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Infinite while loop with drawing screen windows
    while True:
        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip()
        # Exit button execute
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return







if __name__ == "__main__":
    main()