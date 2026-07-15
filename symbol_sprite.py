from reel import SymbolConfig
from settings import SYMBOL_SIZE, OFFSET_Y
import pygame


class SymbolSprite(pygame.sprite.Sprite):
    def __init__(self, symbol_config: SymbolConfig, position: pygame.Vector2, idx: int) -> None:
        super().__init__()
        self.position = position
        self.idx = idx
        self.name = symbol_config.name

        self.image = pygame.image.load(
            symbol_config.image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image, (SYMBOL_SIZE, SYMBOL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (position.x, position.y +  # ty:ignore[invalid-assignment]
                             idx * (SYMBOL_SIZE + OFFSET_Y))

    def set_symbol(self, symbol_config: SymbolConfig) -> None:
        self.name = symbol_config.name
        self.image = pygame.image.load(
            symbol_config.image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image, (SYMBOL_SIZE, SYMBOL_SIZE))
