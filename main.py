# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants

def main():
    pygame.init()
    print("Starting asteroids!") # Print a starting message
    
    # Access screen dimensions from you constants module
    screen_width = constants.SCREEN_WIDTH
    screen_height = constants.SCREEN_HEIGHT


    # Print the dimensions
    print("Screen width:", screen_width)
    print("Screen height:", screen_height)

    # Step 4: Set up the window
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Step 5-7: Create the game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Refresh the screen
        pygame.display.flip()

    # Properly quit pygame
    pygame.quit()


if __name__ == "__main__":
    main() #Call the main function to execute
