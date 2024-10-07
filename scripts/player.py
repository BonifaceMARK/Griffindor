# scripts/player.py
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5
        self.gold = 200  # Starting gold
        self.equipped_items = {  # Track equipped items
            "Weapon": "None",
            "Shield": "None",
            # Add more categories as needed
        }

    def equip_item(self, item_name):
        if item_name in self.equipped_items:
            self.equipped_items["Weapon"] = item_name

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed
