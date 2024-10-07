import pygame  # Import Pygame directly

class Tile(pygame.sprite.Sprite):  # Use pygame.sprite.Sprite directly
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class TileMap:
    def __init__(self, tileset):
        self.tileset = tileset
        self.tile_size = 32

    def load_map(self, map_data):
        tiles = pygame.sprite.Group()  # Use pygame.sprite.Group directly
        for row, tiles_row in enumerate(map_data):
            for col, tile in enumerate(tiles_row):
                x, y = col * self.tile_size, row * self.tile_size
                if tile == '1':  # Example of grass tile
                    image = self.tileset['grass']
                    tile_sprite = Tile(image, x, y)
                    tiles.add(tile_sprite)
        return tiles
