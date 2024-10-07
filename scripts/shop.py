# scripts/shop.py
import pygame

class Shop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.items = {
            "Bow": 100,
            "Sword": 150,
            "Club": 50,
            "Axe": 200
        }
        self.show_shop = False
        self.font = pygame.font.Font(None, 36)

    def toggle_shop(self):
        self.show_shop = not self.show_shop

    def check_proximity(self, player_rect):
        shop_rect = pygame.Rect(self.x, self.y, 200, 200)  # Define shop rectangle area
        return shop_rect.colliderect(player_rect)

    def draw(self, screen):
        if self.show_shop:
            # Draw the shop window
            pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 200, 200))
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 200, 200), 5)  # Window border

            # Draw the items in the shop
            for index, (item, price) in enumerate(self.items.items()):
                text = self.font.render(f"{item}: {price} gold", True, (0, 0, 0))
                screen.blit(text, (self.x + 10, self.y + 30 + index * 30))  # Display items

            # Instructions to buy items
            instruction_text = self.font.render("Press 1-4 to buy", True, (0, 0, 0))
            screen.blit(instruction_text, (self.x + 10, self.y + 150))

    def buy_item(self, item_name, player):
        if item_name in self.items:
            price = self.items[item_name]
            if player.gold >= price:
                player.gold -= price
                player.equip_item(item_name)
                print(f"{item_name} purchased!")
            else:
                print("Not enough gold!")

