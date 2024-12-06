# For generating random height of pipes 
import random
import sys
import pygame
from pygame.locals import *

# Global Variables for the game
window_width = 600
window_height = 499

# Set height and width of window
window = pygame.display.set_mode((window_width, window_height))
elevation = window_height * 0.8
game_images = {}
framepersecond = 32

# File paths for images (ensure these paths are valid in your environment)
pipeimage = "romanpillar(1)(1)(1).png"
background_image = "dragonbackground(1).jpg"
birdplayer_image = "dragonicon(1)(1).png"
sealevel_image = "sealevelimage(1).png"

def flappygame():
    your_score = 0
    horizontal = int(window_width / 5)
    vertical = int(window_width / 2)
    ground = 0
    mytempheight = 100

    # Generating two pipes for blitting on window
    first_pipe = createPipe()
    second_pipe = createPipe()

    # List containing lower pipes
    down_pipes = [
        {'x': window_width + 300 - mytempheight, 'y': first_pipe[1]['y']},
        {'x': window_width + 300 - mytempheight + (window_width / 2), 'y': second_pipe[1]['y']},
    ]

    # List containing upper pipes
    up_pipes = [
        {'x': window_width + 300 - mytempheight, 'y': first_pipe[0]['y']},
        {'x': window_width + 300 - mytempheight + (window_width / 2), 'y': second_pipe[0]['y']},
    ]

    # Pipe velocity along x
    pipeVelX = -4

    # Bird velocity
    bird_velocity_y = -9
    bird_Max_Vel_Y = 10
    bird_Min_Vel_Y = -8
    birdAccY = 1

    bird_flap_velocity = -8
    bird_flapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if vertical > 0:
                    bird_velocity_y = bird_flap_velocity
                    bird_flapped = True

        # Check if the game is over
        game_over = isGameOver(horizontal, vertical, up_pipes, down_pipes)
        if game_over:
            return

        # Check for score
        playerMidPos = horizontal + game_images['flappybird'].get_width() / 2
        for pipe in up_pipes:
            pipeMidPos = pipe['x'] + game_images['pipeimage'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                your_score += 1
                print(f"Your score is {your_score}")

        # Bird movement
        if bird_velocity_y < bird_Max_Vel_Y and not bird_flapped:
            bird_velocity_y += birdAccY
        if bird_flapped:
            bird_flapped = False
        playerHeight = game_images['flappybird'].get_height()
        vertical = vertical + min(bird_velocity_y, elevation - vertical - playerHeight)

        # Move pipes to the left
                # Move pipes to the left
        for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add new pipe if the first pipe crosses the screen
        if 0 < up_pipes[0]['x'] < 5:
            newpipe = createPipe()
            up_pipes.append(newpipe[0])
            down_pipes.append(newpipe[1])

        # Remove pipes that are out of screen
        if up_pipes[0]['x'] < -game_images['pipeimage'][0].get_width():
            up_pipes.pop(0)
            down_pipes.pop(0)

        # Blit game images
        window.blit(game_images['background'], (0, 0))
        for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
            window.blit(game_images['pipeimage'][0], (upperPipe['x'], upperPipe['y']))
            window.blit(game_images['pipeimage'][1], (lowerPipe['x'], lowerPipe['y']))

        window.blit(game_images['sea_level'], (ground, elevation))
        window.blit(game_images['flappybird'], (horizontal, vertical))

        # Display score
        numbers = [int(x) for x in list(str(your_score))]
        width = sum(game_images['scoreimages'][num].get_width() for num in numbers)
        Xoffset = (window_width - width) / 1.1
        for num in numbers:
            window.blit(game_images['scoreimages'][num], (Xoffset, window_width * 0.02))
            Xoffset += game_images['scoreimages'][num].get_width()

        # Refresh game screen
        pygame.display.update()
        framepersecond_clock.tick(framepersecond)


def isGameOver(horizontal, vertical, up_pipes, down_pipes):
    # Define the bird's bounding rectangle
    bird_rect = pygame.Rect(
        horizontal, vertical,
        game_images['flappybird'].get_width(),
        game_images['flappybird'].get_height()
    )

    # Check collision with the ground or sky
    if vertical > elevation - 25 or vertical < 0:
        return True

    # Check collision with upper and lower pipes
    for pipe in up_pipes + down_pipes:
        pipe_rect = pygame.Rect(
            pipe['x'], pipe['y'],
            game_images['pipeimage'][0].get_width(),
            game_images['pipeimage'][0].get_height()
        )
        if bird_rect.colliderect(pipe_rect):  # Check if bird overlaps the pipe
            return True

    return False


def createPipe():
    # Minimum gap between upper and lower pipes
    gap_size = int(window_height / 5.7)

    # Randomly position the lower pipe's top edge
    y2 = random.randint(
        int(gap_size),  # Ensure the pipe leaves space for the gap
        int(window_height - game_images['sea_level'].get_height() - gap_size)
    )
    
    pipeX = window_width + 10  # Start just outside the screen
    
    # Calculate the upper pipe's bottom edge
    y1 = y2 - gap_size - game_images['pipeimage'][0].get_height()
    
    # Return both pipes
    pipe = [
        # Upper pipe
        {'x': pipeX, 'y': y1},
        
        # Lower pipe
        {'x': pipeX, 'y': y2}
    ]
    return pipe


# Main program where the game starts
if __name__ == "__main__":
    # Initialize pygame
    pygame.init()
    framepersecond_clock = pygame.time.Clock()

    # Set the title on the game window
    pygame.display.set_caption('Flappy Bird Game')

    # Load all the images used in the game
    game_images['scoreimages'] = (
        pygame.image.load("D:/flappyimages/0.png").convert_alpha(),
        pygame.image.load("D:/flappyimages/1.png").convert_alpha(),
        pygame.image.load("D:/flappyimages/2.png").convert_alpha(),
        pygame.image.load("D:/flappyimages/3.png").convert_alpha(),
        pygame.image.load("D:/flappyimages/4.png").convert_alpha(),
        pygame.image.load("D:/flappyimages/5.png").convert_alpha(),
        pygame.image.load("D:/flappyimages/6.png").convert_alpha(),
        pygame.image.load("D:/flappyimages/7.png").convert_alpha(),
        pygame.image.load("D:/flappyimages/8.png").convert_alpha(),
        pygame.image.load("D:/flappyimages/9.png").convert_alpha()
    )
    game_images['flappybird'] = pygame.image.load(birdplayer_image).convert_alpha()
    game_images['sea_level'] = pygame.image.load(sealevel_image).convert_alpha()
    game_images['background'] = pygame.image.load(background_image).convert_alpha()
    pipe_width = int(window_width * 0.15)  # Adjust width as a percentage of the screen width
    pipe_height = int(window_height * 1.2)  # Make the pipe tall enough to cover full height

    game_images['pipeimage'] = (
        pygame.transform.rotate(
            pygame.transform.scale(pygame.image.load(pipeimage).convert_alpha(), (pipe_width, pipe_height)), 180
        ),
        pygame.transform.scale(
            pygame.image.load(pipeimage).convert_alpha(), (pipe_width, pipe_height)
        )
    )

    print("WELCOME TO THE FLAPPY BIRD GAME")
    print("Press space or up arrow to start the game")

    # Main game loop
    while True:
        horizontal = int(window_width / 5)
        vertical = int((window_height - game_images['flappybird'].get_height()) / 2)
        ground = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    flappygame()
                else:
                    window.blit(game_images['background'], (0, 0))
                    window.blit(game_images['flappybird'], (horizontal, vertical))
                    window.blit(game_images['sea_level'], (ground, elevation))
                    pygame.display.update()
                    framepersecond_clock.tick(framepersecond)