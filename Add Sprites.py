import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rectangular Sprites Game")

# Define the sprite class
class RectSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0 and keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if self.rect.right < SCREEN_WIDTH and keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if self.rect.top > 0 and keys[pygame.K_UP]:
            self.rect.y -= 5
        if self.rect.bottom < SCREEN_HEIGHT and keys[pygame.K_DOWN]:
            self.rect.y += 5

# Create two sprites
sprite1 = RectSprite(BLUE, 50, 50, 100, 100)  # Movable sprite
sprite2 = RectSprite(RED, 50, 50, 300, 300)    # Static sprite

# Create a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the sprites
    all_sprites.update()

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Refresh the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)