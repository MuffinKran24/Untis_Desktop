import pygame

# Initialize Pygame
pygame.init()

# Set up the display
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('UntisTest')

# Fill the background
screen.fill(background_colour)
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()