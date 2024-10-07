# scripts/camera.py
import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        # Keep the camera within the bounds of the level
        x = min(0, x)  # Left boundary
        x = max(-(self.width - self.width), x)  # Right boundary
        y = min(0, y)  # Top boundary
        y = max(-(self.height - self.height), y)  # Bottom boundary

        self.camera = pygame.Rect(x, y, self.width, self.height)
