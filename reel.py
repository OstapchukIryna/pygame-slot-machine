
import pygame
import random
from settings import *
from symbol_sprite import SymbolSprite


class Reel:
    def __init__(self, pos: pygame.Vector2, symbols: dict[str, SymbolConfig]) -> None:
        self.pos = pos
        # {"cherry": {"weight": 10, "image_path": "..."}, ...}
        self.symbols = symbols
        self.symbol_sprites = pygame.sprite.Group()
        self.is_spinning = False

    def _pick_random_symbols(self, count: int = 5) -> list[str]:
        names = list(self.symbols.keys())
        weights = [self.symbols[name].weight for name in names]
        return random.choices(names, weights=weights, k=count)

    def spin(self) -> None:
        chosen = self._pick_random_symbols()
        self.symbol_sprites.empty()
        for i, symbol_name in enumerate(chosen):
            sprite = SymbolSprite(self.symbols[symbol_name], self.pos, i)
            self.symbol_sprites.add(sprite)

    def update(self, dt):
        pass

    def draw(self, screen: pygame.Surface) -> None:
        self.symbol_sprites.draw(screen)

        # TODO add sounds
        # self.stop_sound = pygame.mixer.Sound("audio/stop.mp3")
        # self.stop_sound.set_volume(0.5)
