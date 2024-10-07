import pygame
import random
import sys
from scripts.player import Player
from scripts.enemy import Enemy
from scripts.tilemap import TileMap
from scripts.shop import Shop
from scripts.camera import Camera

# Initialize Pygame
pygame.init()

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Medieval MMORPG")

# Load the shop image after the display has been created
shop_image = pygame.image.load('assets/shop.png').convert_alpha()

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()  # Group for enemies
player = Player(100, 100)  # Initial position of the player
all_sprites.add(player)

# Create some enemies
for i in range(5):  # Create 5 enemies
    enemy = Enemy(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
    enemies.add(enemy)
    all_sprites.add(enemy)

# Load tile images
tileset = {
    'grass': pygame.image.load('assets/grass.png').convert()
}

# Define the map layout (simple example)
map_data = [
    '11111111',
    '10000001',
    '10000001',
    '10000001',
    '11111111'
]

# Create the tilemap
tilemap = TileMap(tileset)
tiles = tilemap.load_map(map_data)

# Initialize the camera
camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)  # Pass the screen dimensions

# Create the shop
shop = Shop(10, 10)  # Place the shop in the upper left corner

# Equipment bar items
equipment_bar_items = ["Bow", "Sword", "Club", "Axe"]
equipped_items = ["None", "None", "None", "None"]  # Initialize with no equipped items

def draw_equipment_bar():
    bar_height = 50
    pygame.draw.rect(screen, (0, 0, 0), (0, SCREEN_HEIGHT - bar_height, SCREEN_WIDTH, bar_height))  # Bar background

    # Draw equipped items
    for i, (key, item) in enumerate(player.equipped_items.items()):
        # Display equipped items
        text = pygame.font.Font(None, 36).render(f"{key}: {item}", True, (255, 255, 255))
        screen.blit(text, (10 + i * 200, SCREEN_HEIGHT - bar_height + 10))  # Spacing between items

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for item purchase when the shop is shown
            if shop.show_shop:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        shop.buy_item("Bow", player)
                    elif event.key == pygame.K_2:
                        shop.buy_item("Sword", player)
                    elif event.key == pygame.K_3:
                        shop.buy_item("Club", player)
                    elif event.key == pygame.K_4:
                        shop.buy_item("Axe", player)

        # Get keys pressed for player movement
        keys_pressed = pygame.key.get_pressed()

        # Update the player with keys_pressed
        player.update(keys_pressed)

        # Update enemies
        enemies.update()

        # Fill screen with a color (background)
        screen.fill((50, 50, 50))

        # Update camera position based on player
        camera.update(player)

        # Draw the tiles and sprites with the camera
        for tile in tiles:
            screen.blit(tile.image, camera.apply(tile))
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))

        # Check if player is near the shop
        if shop.check_proximity(player.rect):
            shop.toggle_shop()  # Toggle the shop window
        else:
            shop.show_shop = False  # Hide shop if player is not near

        # Draw the shop if it's activated
        shop.draw(screen)

        # Draw the equipment bar at the bottom
        draw_equipment_bar()

        # Update display
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()
