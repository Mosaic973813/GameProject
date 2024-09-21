# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    pygame.init()
    #print("Starting asteroids!") # Print a starting message
    
    # Access screen dimensions from you constants module
    #screen_width = constants.SCREEN_WIDTH
    #screen_height = constants.SCREEN_HEIGHT


    # Print the dimensions
    #print("Screen width:", screen_width)
    #print("Screen height:", screen_height)

    # Step 4: Set up the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    # Creates groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    


    # Step 5-7: Create the game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         new_shot = player.shoot()
            #         shots.add(new_shot)
            #         updatable.add(new_shot)
            #         drawable.add(new_shot)

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()



        # Fill the screen with black
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        #asteroid_field.update(dt) # Handles timing for when to spawn


        #pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100)) #Draw a red rectangle
        #player.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Control the frame rate
        dt = clock.tick(60) / 1000


    # Properly quit pygame
    #pygame.quit()


if __name__ == "__main__":
    main() #Call the main function to execute
