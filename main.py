import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Boot text
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Infinite loop with exit button execution
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Window fill with black color and constantly refreshing 
        screen.fill("black")
        pygame.display.flip()






if __name__ == "__main__":
    main()
