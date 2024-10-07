import pygame
import random

class Enemy(pygame.sprite.Sprite):  # Inherit from pygame.sprite.Sprite directly
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/enemy.png').convert_alpha()  # Load your enemy image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = random.randint(1, 3)  # Random speed for some variety

    def update(self):
        # Simple movement behavior (for example, moving left and right)
        self.rect.x += self.speed

        # Reverse direction when reaching the screen edge
        if self.rect.left < 0 or self.rect.right > pygame.display.get_surface().get_width():
            self.speed = -self.speed

    def attack(self, player):
        # Placeholder for attack logic
        if self.rect.colliderect(player.rect):
            print("Enemy attacks the player!")
            # Implement damage logic here
